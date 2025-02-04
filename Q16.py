'''
•	16. Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.


'''

from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod 
    def calculate_area(self):
        pass
    
class Rectangle(IShape):
    def calculate_area(self , side):
        print('area',side*side)

class Circle(IShape):
    def calculate_area(self,radius):
        print(f'area {(3.14)*(radius*radius)}')
rectangle=Rectangle()
rectangle.calculate_area(90)
circle=Circle()
circle.calculate_area(10)