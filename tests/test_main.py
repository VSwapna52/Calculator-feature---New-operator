import pytest
from src.main import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_addition(calculator):
    assert calculator.calculate(2, 3, '+') == 5

def test_subtraction(calculator):
    assert calculator.calculate(5, 3, '-') == 2

def test_multiplication(calculator):
    assert calculator.calculate(2, 3, '*') == 6

def test_division(calculator):
    assert calculator.calculate(6, 3, '/') == 2

def test_cat_operator(calculator):
    assert calculator.calculate(2, 3, '🐇') == 13
    assert calculator.calculate(1, 3, '🐇') == 11
    assert calculator.calculate(2, 2, '🐇') == 10

def test_clear(calculator):
    calculator.clear()
    assert calculator.current_value == 0

def test_equals(calculator):
    calculator.calculate(2, 3, '+')
    assert calculator.calculate(0, 0, '=') == 5

def test_invalid_operation(calculator):
    with pytest.raises(ValueError):
        calculator.calculate(2, 3, '%')