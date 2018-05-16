import operator


def _convert(value):
    """This function converts string to int or float, but keeps operators as string.

    >>> _convert("1")
    1

    >>> _convert("1.0")
    1.0

    >>> _convert("+")
    '+'

    """
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

    """
    >>> calc = Calculator()
    >>> calc.process_string("1 1 +")
    >>> calc.pop()
    2

    """

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
