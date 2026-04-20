# Drone Mission Planner
#### Video Demo: https://youtu.be/85jDRyjy_Ww
#### Description:

I am Daniel Ojo, a Computer Science student from Lagos, Nigeria.
My long term goal is to become a Flight Software Engineer
specialising in satellite systems. This project is my CS50x
2026 final project and it reflects that goal.

The Drone Mission Planner is a simple terminal tool built in
Python. You give it a destination, your drone speed, your
battery capacity and consumption rate, and it tells you
everything you need to know about the mission before your
drone ever takes off. It also saves the report to a text file
automatically.

## How to Run

```bash
python project.py
```

When it runs, enter your inputs one by one. After the
calculation, check `mission_log.txt` for the full saved report.

## Inputs

- Destination X coordinate — how far East in metres
- Destination Y coordinate — how far North in metres
- Drone speed in m/s
- Available battery in mAh
- Battery consumption rate in mAh per second

## Outputs

- **Destination** — the coordinates you entered
- **Distance** — straight line distance from home to destination
- **Speed** — your entered speed
- **Flight Time** — how long the full round trip takes in seconds
- **Battery Consumption** — your entered consumption rate
- **Required Battery** — total battery the round trip needs
- **Available Battery** — battery you entered
- **Mission Feasible** — True if you have enough battery, False if not

Everything prints to terminal and saves to `mission_log.txt`.

## How the Maths Works

Home base is always (0, 0). The destination is wherever
you enter on the x/y grid in metres.

The drone flies a straight diagonal line to the destination
and back. Distance uses Pythagoras:

    distance = sqrt(x squared + y squared)

Round trip is double that. Flight time is distance divided
by speed. Battery needed is flight time multiplied by
consumption rate. Then it checks if your battery covers it.

## Why I Built It This Way

I chose a delivery mission because it is the simplest and
most honest version of drone mission planning. One drone,
one destination, go there and come back. No unnecessary
complexity.

I used a simple x/y coordinate grid instead of real GPS
coordinates because the maths is the same and it is much
easier to understand and test. The concept is identical to
what real flight planning software does.

The `check_feasibility()` function returns a dictionary
instead of just a string. I did this so the same data
works for both the terminal output and the file export
without calculating anything twice.

The `format_number()` function removes unnecessary decimal
places. If you enter a whole number it shows as a whole
number. If the calculation produces a decimal it shows the
decimal. Cleaner output for the user.

I chose the delivery mission over patrol or search grid
because I wanted to submit something complete and working
rather than something ambitious and broken.

## Files

- `project.py` — the main program
- `test_project.py` — three pytest tests for core functions
- `mission_log.txt` — auto generated after every run
- `README.md` — this file

## Tests

```bash
pytest test_project.py
```

Three tests covering:
- Distance calculation using the 3, 4, 5 triangle
- Flight time equals distance divided by speed
- Battery equals flight time multiplied by consumption rate

All three pass at 100%.
