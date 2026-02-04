from Calculator import square
import Calculator
import importlib

# Reload to avoid cache issues
importlib.reload(Calculator)

def test_square_positive():
    assert square(2) == 4

def test_square_negative():
    assert square(-2) == 4

def test_square_zero():
    assert square(0) == 0

print("Calculator module path:", Calculator.__file__)
