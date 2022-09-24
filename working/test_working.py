from working import convert
import pytest


def main():
    test_correct_time()
    test_wrong_minutes()
    test_wrong_hours()
    test_wrong_format()


def test_correct_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("12:00 AM to 8:50 AM") == "00:00 to 08:50"
    assert convert("12:00 PM to 8:50 AM") == "12:00 to 08:50"



def test_wrong_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_wrong_hours():
    with pytest.raises(ValueError):
        convert("20:00 AM to 20:00 PM")


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


if __name__ == "__main__":
    main()