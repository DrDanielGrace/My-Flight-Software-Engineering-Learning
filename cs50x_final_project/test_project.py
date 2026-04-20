from project import calculate_distance, calculate_flight_time, calculate_battery


def test_calculate_distance():
    # x coordinate is 3, y coordinate is 4
    assert calculate_distance(3, 4) == 5.0


def test_calculate_flight_time():
    # distance is 100m, speed is 10m/s
    assert calculate_flight_time(100, 10) == 10.0


def test_calculate_battery():
    # Flight time is 10s, battery consumption rate is 100mAh/s
    assert calculate_battery(10, 100) == 1000.0
