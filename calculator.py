import operator


def _convert(value):
    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    return value


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

    def process_string(self, expression):
        for value in expression.split(' '):
            self.push(_convert(value))

    def process_file(self, filename):
        with open(filename) as f:
            for line in f:
                self.process_string(line)
