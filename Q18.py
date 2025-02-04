'''
•	18. Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator` class that implements these methods.
'''
from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def subtract(self):
        pass
    @abstractmethod
    def mulitply(self):
        pass
    @abstractmethod
    def divide(self):
        pass
class BasicCalculator(ICalculator):
    def add(self,a,b):
        print('addition',a+b)
    def subtract(self,a,b):
        print('subtraction',a-b)
    def divide(self,a,b):
        print('divsion',a/b)
    def mulitply(self,a,b):
        print('multiplicaiton',a*b)
calc=BasicCalculator()
calc.add(1,2)
calc.subtract(6,2)
calc.mulitply(1,2)
calc.divide(1,2)