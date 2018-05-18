import os.path
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


def test_div_by_zero(calculator):
    calculator.push(2)
    calculator.push(0)
    with pytest.raises(ZeroDivisionError):
        calculator.push('/')


def test_record(calculator, tmpdir):
    operations = "1 1 + 1 + 1 +"
    record_file = tmpdir.join('record.txt')

    with calculator.recorder(record_file):
        calculator.process_string(operations)
    
    assert os.path.exists(record_file)
    with open(record_file) as f:
        saved_record = f.read()
    assert operations == saved_record.strip()
