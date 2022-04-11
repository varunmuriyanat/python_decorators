class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535


c = Circle(10)
print(f"The radius is {c.radius}")
print(f"The area is {c.area}")

c.radius = 100
print(f"The radius is {c.radius}")
print(f"The area is {c.area}")

print(f"The area is {c.cylinder_volume(4)}")

c1 = Circle.unit_circle() 
print(f"Unit circle radius is {c1.radius}")


print(f"pi is {c1.pi()}")
print(f"pi is {Circle.pi()}")

