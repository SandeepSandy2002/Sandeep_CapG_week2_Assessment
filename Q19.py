'''
•	19. Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. Implement it in `Car`, `Bike`, and `Truck` classes.
'''
from abc import ABC, abstractmethod

class IVehicle(ABC):
    
    @abstractmethod 
    def start_engine(self):
        pass
    @abstractmethod 
    def stop_engine(self):
        pass
    
class Car(IVehicle):
    def start_engine(self):
        print('car engine started')
    def stop_engine(self):
        print('car engine stopped')

class Bike(IVehicle):
    def start_engine(self):
        print('bike engine started')
    def stop_engine(self):
        print('bike engine stopped')

class Truck(IVehicle):
    def start_engine(self):
        print('truck engine started')
    def stop_engine(self):
        print('truck engine stopped')
        
car=Car()
car.start_engine()
car.stop_engine()
bike=Bike()
bike.start_engine()
bike.stop_engine()
truck=Truck()
truck.start_engine()
truck.stop_engine()