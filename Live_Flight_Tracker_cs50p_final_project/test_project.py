from project import format_altitude, format_speed, parse_flights


def test_format_altitude():
    assert format_altitude(None) == "Plane still on ground"
    assert format_altitude(731) == "2398 ft"
    assert format_altitude(10668) == "FL350"

def test_format_speed():
    assert format_speed(None) == "Plane yet to move"
    assert format_speed(35) == "68 kts"
    assert format_speed(257) == "500 kts"

def test_parse_flights():
    fake_flights = [
        [None, "DAL1074", "United States", None, None, None, None, 10000, 12000, 250, 120]
    ]

    result = parse_flights(fake_flights)
    assert result[0]["callsign"] == "DAL1074"
    assert result[0]["country"] == "United States"
    assert result[0]["altitude"] == "FL328" #10000 metres to feet to altitude
    assert result[0]["speed"] == "486 kts" #250 m/s to kts

