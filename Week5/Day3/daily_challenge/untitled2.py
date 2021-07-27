class Circle():
    def __init__(self, **kwargs):
        if 'diameter' in kwargs:
            self.diameter = kwargs['diameter']
            self.radius()
        elif 'radius' in kwargs:
            self.radius = kwargs['radius']
            self.diameter()
        else:
            self.radius = 1
    def diameter(self):
        self.diameter = self.radius * 2
        return self.diameter
    def radius(self):
        self.radius = self.diameter / 2
        return self.radius
    def area(self):
        return 3.14159265 * (self.radius ** 2)
    def __eq__(self, other):
        return self.radius == other.radius
    def __ge__(self, other):
        return self.radius >= other.radius
    def __le__(self, other):
        return self.radius <= other.radius
    def __ne__(self, other):
        return self.radius != other.radius
    def __lt__(self, other):
        return self.radius < other.radius
    def __gt__(self, other):
        return self.radius > other.radius
    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)
    def __str__(self):
        return 'circle:radius:' + str(self.radius)

circle = Circle(radius=1)
print(circle.area())
print(*sorted([Circle(radius=3), Circle(radius=2), Circle(radius=7)]))
