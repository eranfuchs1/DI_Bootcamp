class Circle():
    def __init__(self, **kwargs):
        if 'diameter' in kwargs:
            self.d = kwargs['diameter']
            self.radius()
        elif 'radius' in kwargs:
            self.r = kwargs['radius']
            self.diameter()
        else:
            self.radius = 1
    def diameter(self):
        self.d = self.r * 2
        return self.d
    def radius(self):
        self.r = self.d / 2
        return self.r
    def area(self):
        return 3.14159265 * (self.r ** 2)
    def __eq__(self, other):
        return self.r == other.r
    def __ge__(self, other):
        return self.r >= other.r
    def __le__(self, other):
        return self.r <= other.r
    def __ne__(self, other):
        return self.r != other.r
    def __lt__(self, other):
        return self.r < other.r
    def __gt__(self, other):
        return self.r > other.r
    def __add__(self, other):
        return Circle(radius=self.r + other.r)
    def __str__(self):
        return 'circle:radius:' + str(self.r)

circle = Circle(radius=1)
print(circle.area())
print(*sorted([Circle(radius=3), Circle(radius=2), Circle(radius=7)]))
