from working import convert
import pytest

def test_valid_time_formats():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:15 AM to 10:15 PM") == "10:15 to 22:15"


def test_invalid_time_formats():
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM to 7:00 AM")  # More than two time ranges
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")  # Invalid minutes
    with pytest.raises(ValueError):
        convert("9:00 AM to 15:00 PM")  # Invalid time format


def test_out_of_range_times():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")  # Invalid start time
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")  # Invalid end time