import csv
import datetime
import requests
import sys


def main():

    # Get the user location
    location = input("Enter your location: ")

    if not location:
        sys.exit("Location cannot be empty. Please enter a valid location")

    if location.isdigit():
        sys.exit("Location cannot be a digit.")

    if len(location) < 2:
        sys.exit("Location name too short. Pls be more specific")

    min_lat, max_lat, min_lon, max_lon = get_coordinates(location)
    flights = get_flights(min_lat, max_lat, min_lon, max_lon)
    flights_data = parse_flights(flights)

    # Get the user current date
    now = datetime.datetime.now()
    date = now.strftime("%dth of %B %Y")
    time = now.strftime("%H:%M:%S")

    # Output the results
    print_header(location, date, time, flights_data)

    print_flights(flights_data)

    print_footer()

    save_to_csv(location, flights_data)
    save_to_txt(location, date, time, flights_data)

    print("""
Thanks for your time. Hope to see you soon.""")


# Function that gets a location name eg "Lagos" and converts it a coordinate using Nominatim api for OpenSky to understand
def get_coordinates(location):
    # Makes the API call with params
    response = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={"q": location, "format": "json", "limit": 1},
        headers={"User-Agent": "live-flight-tracker"},
    )

    # Parse the json files
    data = response.json()

    # Exit for location not found
    if not data:
        sys.exit("Location not found. Try being more specific, eg: Lagos, Nigeria")

    # Extracts the location coordinate bounding box
    bounding_box = data[0]["boundingbox"]
    # Unpacks the longitude and lattitude coordinates (east, west, north, south)
    min_lat, max_lat, min_lon, max_lon = bounding_box
    return min_lat, max_lat, min_lon, max_lon


# Function that uses the get_coordinates and querys OpenSky Api to get raw flight data of planes over those coordinates
def get_flights(min_lat, max_lat, min_lon, max_lon):
    # Expand the bounding box to get more flights around the area
    padding = 0
    min_lat = float(min_lat) - padding
    max_lat = float(max_lat) + padding
    min_lon = float(min_lon) - padding
    max_lon = float(max_lon) + padding

    # Make Api calls to OpenSky URL
    response = requests.get(
        "https://opensky-network.org/api/states/all",
        params={
            "lamin": min_lat,
            "lamax": max_lat,
            "lomin": min_lon,
            "lomax": max_lon,
        },
    )

    # Parse the json file
    data = response.json()

    # Exit if no flights found
    if not data["states"]:
        sys.exit("There are no flights in this area, Try Again later")

    states = data["states"]
    return states


# Pull out the needed flight data from get_flights and cleans it for proper output
def parse_flights(flights):

    # Empty list to store the flight data
    cleaned_flights = []

    for flight in flights:
        # We extract specific items from raw get_flights data
        callsign = flight[1].strip()
        country = flight[2]
        altitude = flight[7]
        speed = flight[9]

        flight_dict = {
            "callsign": callsign,
            "country": country,
            "altitude": format_altitude(altitude),
            "speed": format_speed(speed),
        }

        # Adds the flightDict to the cleaned list
        cleaned_flights.append(flight_dict)

    return cleaned_flights

# Saves data to csv file
def save_to_csv(location, flights_data):
    filename = f"flights_{location.replace(' ', '_')}.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["callsign", "country", "altitude", "speed"]
        )
        writer.writeheader()
        writer.writerows(flights_data)

    print(f"CSV Flight Data saved to {filename}.")


# Saves formatted data to txt file
def save_to_txt(location, date, time, flights_data):
    filename = f"flights_{location.replace(' ', '_')}.txt"

    with open(filename, "w") as file:
        sys.stdout = file  # redirects the terminal print to file
        print_header(location, date, time, flights_data)
        print_flights(flights_data)
        print_footer()
        sys.stdout = sys.__stdout__  # restore terminal output

    print(f"Formatted Flight Data saved to {filename}.")


# Function that converts altitude in meters to feets and flight level
def format_altitude(altitude_meters):
    if altitude_meters is None:
        return "Plane still on ground"

    # Convert meters to feet
    feet = float(altitude_meters * 3.28084)

    if feet <= 18000:
        return f"{feet:.0f} ft"
    else:
        flight_level = int(feet / 100)
        return f"FL{flight_level}"


# Function that converts speed from m/s to knots (nautical / hour)
def format_speed(speed_ms):
    if speed_ms is None:
        return "Plane yet to move"
    knots = float(speed_ms * 1.94384)
    return f"{knots:.0f} kts"


# Function to print header texts
def print_header(location, date, time, flights_data):
    print("""================================================
LIVE FLIGHT TRACKER
================================================""")
    print(f"Location: {location}")
    print(f"Date: {date}")
    print(f"Time: {time} UTC")
    print(f"Total Flights Found: {len(flights_data)}")
    print("================================================")


def print_flights(flights_data):
    # Loops thrugh each flight data and output the results
    for index, flight in enumerate(flights_data, 1):
        callsign = (
            flight["callsign"].strip() if flight["callsign"].strip() else "Unknown"
        )
        country = flight["country"]
        altitude = flight["altitude"]
        speed = flight["speed"]

        print(
            f"{index}. Callsign: {callsign} || Reg. Country: {country} || Altitude: {altitude} || Speed: {speed}"
        )


# Function that prints footer details
def print_footer():
    print("================================================")
    print("Made with love by Daniel Grace")
    print("Live Data sourced from OpenSky Network and Nominatim")
    print("================================================")


if __name__ == "__main__":
    main()
