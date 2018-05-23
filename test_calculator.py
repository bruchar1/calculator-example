from contextlib import contextmanager
import os.path
import pytest
from calculator import Calculator


@pytest.fixture()
def calculator():
    return Calculator()


@pytest.mark.parametrize("operations, result", [
    ("1 1 +", 2),
    ("1 1 -", 0),
    ("1 2 *", 2),
    ("2 2 /", 1)
])
def test_process(calculator, operations, result):
    calculator.process_string(operations)
    assert result == calculator.pop()


@pytest.fixture(params=[
    ("1 1 +", 2),
    ("1 1 -", 0),
    ("1 2 *", 2),
    ("2 2 /", 1)
])
def process_fixture(calculator, request):
    operations, result = request.param
    calculator.process_string(operations)
    return calculator, result

def test_operations(process_fixture):
    calculator, result = process_fixture
    assert result == calculator.pop()


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


def test_process_file(calculator, monkeypatch):
    @contextmanager
    def fake_open(*args, **kwargs):
        yield ["1 1 +", "2 +"]
    
    monkeypatch.setattr(calculator, "_open", fake_open)

    calculator.process_file("filename")
    assert calculator.pop() == 4


def test_process_string(calculator, mocker):
    push_spy = mocker.spy(calculator, "push")
    pop_spy = mocker.spy(calculator, "pop")

    calculator.process_string("1 1 +")
    assert push_spy.call_count == 3
    assert pop_spy.call_count == 2
