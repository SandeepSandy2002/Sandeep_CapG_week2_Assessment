class Shape:
    def area(self):
        print('The area of below shape')
        # Default implementation (could be changed in subclasses)

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


square = Square(4)
triangle = Triangle(3, 6)
print(square.area())
print(f"Area of the square: {square.area()}")  
print(f"Area of the triangle: {triangle.area()}") 
