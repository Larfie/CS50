from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_convert_zero_error()
    test_convert_value_error()


def test_convert():
    assert convert("10/100") == 10


def test_convert_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("a/t")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


if __name__ == "__main__":
    main()
