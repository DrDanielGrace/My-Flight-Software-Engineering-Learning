import math


def main():
    #  Infinite loop to Ask user for floating inputs
    while True:
        try:
            x = float(input("Input your x coordinates: "))
            y = float(input("Input your y coordinates: "))
            speed = float(input("Drone Speed (m/s): "))
            battery_capacity = float(input("Available Battery (mAh): "))
            consumption_rate = float(input("Battery Consumption Rate (mAh/s): "))
            break

        except ValueError:
            continue

    # Variables that stores all the calculated data
    distance = calculate_distance(x, y)
    flight_time = calculate_flight_time(distance, speed)
    required_battery = calculate_battery(flight_time, consumption_rate)
    feasible = check_feasibility(battery_capacity, required_battery)

    # Dictionary that takes all the data
    data = {
        "x": x,
        "y": y,
        "distance": distance,
        "speed": speed,
        "battery_capacity": battery_capacity,
        "consumption_rate": consumption_rate,
        "flight_time": flight_time,
        "required_battery": required_battery,
        "feasible": feasible["feasible"],
        "extra_battery": feasible["extra_battery"],
        "short_fall": feasible["short_fall"],
    }

    # exports the data to mission log file
    export_mission(data, "mission_log.txt")


# Function to calculate the distance in metres using pythagoras theorem
def calculate_distance(x, y):
    distance = math.sqrt(x**2 + y**2)
    return distance


# Function to dynamic format numbers for either int or float when required
def format_number(n):
    return int(n) if n == int(n) else round(n, 2)


# Function to calculate flight time using calculated distance and inputted speed
def calculate_flight_time(distance, speed):
    # Time = Distance / Speed
    flight_time = float(distance / speed)
    return flight_time


# Function to calculate the drone battery for the flight return unit in mAh
def calculate_battery(flight_time, consumption_rate):
    required_battery = flight_time * consumption_rate
    return required_battery


# Function to check if battery can be used for the flight
def check_feasibility(battery_capacity, required_battery):

    if required_battery <= battery_capacity:
        return {
            "feasible": True,
            "extra_battery": battery_capacity - required_battery,
            "short_fall": 0,
        }
    else:

        return {
            "feasible": False,
            "extra_battery": 0,
            "short_fall": required_battery - battery_capacity,
        }


def export_mission(data, filename):
    mission_log = f"""Destination: ({format_number(data["x"])} x, {format_number(data["y"])} y)
Distance (m): {format_number(data["distance"])}m
Speed: {format_number(data["speed"])} m/s
Flight Time: {format_number(data["flight_time"])}s
Battery Consumption: {format_number(data["consumption_rate"])} mAh/s
Required Battery: {format_number(data["required_battery"])} mAh
Available Battery: {format_number(data["battery_capacity"])} mAh
Mission Feasible: {data["feasible"]}
"""
    with open("mission_log.txt", "w") as file:
        file.write(mission_log)

    print(mission_log)  # variable that stores the data in the export_mission function
    print("Mission saved to mission_log.txt")


if __name__ == "__main__":
    main()
