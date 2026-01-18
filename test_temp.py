import pytest
from temp import celsius_to_fahrenheit

def test_zero_celsius():
    assert celsius_to_fahrenheit(0) == 32

def test_positive_celsius():
    assert celsius_to_fahrenheit(25) == 77

def test_negative_celsius():
    assert celsius_to_fahrenheit(-40) == -40
