from calculator import Calculator

import pytest
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.stateful import Bundle, RuleBasedStateMachine, rule
import math


@given(st.tuples(st.one_of(st.integers(), st.floats()),
                 st.one_of(st.integers(), st.floats()),
                 st.sampled_from(('+', '-', '*', '/'))).filter(
                     lambda x: not (x[1] == 0 and x[2] == '/')
                 ))
def test_binary_operation(args):
    a, b, op = args
    calculator = Calculator()
    calculator.push(a)
    calculator.push(b)
    calculator.push(op)
    result = calculator.pop()

    eval_result = eval("{} {} {}".format(a, op, b),
                       {}, {"inf": float("inf"),
                            "nan": float("nan")})

    if math.isnan(eval_result):
        assert math.isnan(result)
    else:
        assert eval_result == result


class CalculatorStateMachine(RuleBasedStateMachine):
    
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
    
    @rule(n=st.one_of(st.integers(), st.floats()))
    def push_number(self, n):
        self.calculator.push(n)
    
    @rule(op=st.sampled_from(('+', '-', '*', '/')))
    def push_operation(self, op):
        self.calculator.push(op)

    @rule()
    def pop_result(self):
        self.calculator.pop()


TestCalculatorStateMachine = CalculatorStateMachine.TestCase
