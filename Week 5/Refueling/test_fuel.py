from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    with pytest.raises(ZeroDivisionError):
        convert('100/0')
    with pytest.raises(ValueError):
        convert('a/b')
    with pytest.raises(ValueError):
        convert('5/2')


def test_guage():
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"