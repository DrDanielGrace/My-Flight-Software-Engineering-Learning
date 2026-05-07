# Live Flight Tracker

#### Video Demo: https://youtu.be/PTuW3GHoPZ4

#### Description:
Live Flight Tracker is a Python tool that tracks all flights currently flying over any location you search for. It pulls live data straight from the sky and shows you each flight's callsign, registration country, altitude, and speed. Results print to your terminal, and also get saved to a CSV file for data use and a TXT file if you want the formatted version.

## How to Use
1. Run the program: `python project.py`
2. Type in any city, state, or country when prompted e.g. `London, United Kingdom`
3. View all flights over that location in your terminal
4. Check your folder for two generated files:
   - `flights_London.csv` for raw data
   - `flights_London.txt` for the formatted report

That's it.

## How it Works
1. You type a location
2. `get_coordinates()` sends that location to the Nominatim OpenStreetMap API and gets back the coordinates of that area
3. `get_flights()` takes those coordinates and asks the OpenSky Network API for all flights currently in that airspace
4. `parse_flights()` cleans the raw data and pulls out what matters
5. The results print to your terminal and save to both a CSV and TXT file

## Dependencies
- `requests` - makes the HTTP calls to both APIs
- `python-dotenv` - manages environment variables
- `csv` - built into Python, handles CSV file creation
- `datetime` - built into Python, gets current date and time
- `sys` - built into Python, handles clean error exits

Install external dependencies with:
pip install -r requirements.txt

## Limitations
Coverage depends entirely on OpenSky Network's ground receiver infrastructure. The network works well in Europe, North America, India, and parts of Asia. Sub-Saharan Africa including Nigeria has very limited coverage because there are very few ADS-B ground receivers in the region. As a Nigerian developer I ran into this firsthand when testing over Lagos and got zero results despite flights clearly being visible on FlightRadar24. This is a known OpenSky limitation, not a bug in the code.

## Future Improvements

### V2 Features
- Departure airport
- Destination airport
- Home country of aircraft
- Distance to destination
- Time already in flight
- Estimated time remaining to destination
- Status flags: "About to take off" / "Just landed"

See `features.txt` for the full version roadmap.

#### Made with love by [Daniel Grace](https://x.com/drdanielgrace)
#### Live Data sourced from [OpenSky Network](https://opensky-network.org) and [Nominatim](https://nominatim.openstreetmap.org)
