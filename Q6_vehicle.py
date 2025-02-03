class vehicle:
    def __init__(self):
        self.usage='taxi'
class bike(vehicle):
    def __init__(self):
        super().__init__()
        self.name='bike'
        self.type='petrol'
        self.wheels=2
class car(vehicle):
    def __init__(self):
        super().__init__()
        self.name='car'
        self.type='diesel'
        self.wheels=4
class electric_car(car):
     def __init__(self):
        super().__init__()
        self.type='electric'
ob1=bike()
print(ob1.usage)
print(ob1.name)
print(ob1.type)
print(ob1.wheels)
ob2=car()
print(ob2.usage)
print(ob2.name)
print(ob2.type)
print(ob2.wheels)
ob3=electric_car()
print(ob3.usage)
print(ob3.name)
print(ob3.type)
print(ob3.wheels)


