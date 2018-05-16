import pytest
from calculator import Calculator


@pytest.fixture()
def calculator():
    return Calculator()

def test_add(calculator):
    calculator.push(1)
    calculator.push(1)
    calculator.push('+')
    assert 2 == calculator.pop()

def test_sub(calculator):
    calculator.push(1)
    calculator.push(1)
    calculator.push('-')
    assert 0 == calculator.pop()

def test_mul(calculator):
    calculator.push(1)
    calculator.push(2)
    calculator.push('*')
    assert 2 == calculator.pop()

def test_div(calculator):
    calculator.push(2)
    calculator.push(2)
    calculator.push('/')
    assert 1 == calculator.pop()
