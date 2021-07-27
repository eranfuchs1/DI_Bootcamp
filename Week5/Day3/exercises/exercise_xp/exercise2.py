class Currency():
    def __init__(self, sign, value):
        self.sign = sign
        self.value = value
    def __int__(self):
        return int(self.value)
    def __repr__(self):
        return f'{self.value} {self.sign}'
    def __add__(self, other):
        if isinstance(other, Currency):
            if not other.sign == self.sign:
                raise ValueError
            return Currency(self.sign, self.value + other.value)
        elif isinstance(other, (int, float)):
            return Currency(self.sign, self.value + other)
