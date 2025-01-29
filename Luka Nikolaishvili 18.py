import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        per = self.perimeter() / 2
        return math.sqrt(per * (per - self.a) * (per - self.b) * (per - self.c))

    def __str__(self):
        return (f"samkutxedis perimetri: {self.perimeter()}\n"
                f"samkutxedis fartobi: {self.area()}\n")


triangle1 = Triangle(3, 4, 5)
triangle2 = Triangle(7, 8, 9)


print(triangle1)
print(triangle2)
