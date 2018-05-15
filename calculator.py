import operator


class Calculator(object):

    OPERATORS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
        }

    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        if value in self.OPERATORS:
            b = self.pop()
            a = self.pop()
            self.stack.append(self.OPERATORS[value](a, b))
        else:
            self.stack.append(value)


if __name__ == '__main__':
    calc = Calculator()
    calc.push(1)
    calc.push(1)
    calc.push('+')
    print(calc.pop())
