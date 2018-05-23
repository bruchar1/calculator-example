from contextlib import contextmanager
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
        if not self.stack:
            return False
        return self.stack.pop()

    def push(self, value):
        if value in self.OPERATORS:
            b = self.pop()
            a = self.pop()
            if a is False or b is False:
                return False
            self.stack.append(self.OPERATORS[value](a, b))
        else:
            self.stack.append(value)
        return True

    def process_string(self, expression):
        for value in expression.split(' '):
            self.push(_convert(value))
    
    @contextmanager
    def _open(self, *args, **kwargs):
        with open(*args, **kwargs) as f:
            yield f

    def process_file(self, filename):
        with self._open(filename) as f:
            for line in f:
                self.process_string(line)

    @contextmanager
    def recorder(self, record_file):
        original_push = self.push

        with self._open(record_file, 'w') as f:
            def record_push(value):
                original_push(value)
                print(value, end=" ", file=f)

            self.push = record_push
            yield
            self.push = original_push
