class Car:
    def move(self):
        return "The car is driving on the road."

class Airplane:
    def move(self):
        return "The airplane is flying in the sky."

class FlyingCar(Car, Airplane):
    def move(self,mode):
        
        if mode == "car":
            return Car.move(self)
        else:
            return Airplane.move(self)


flying_car = FlyingCar()
print(flying_car.move('car')) ##ENTER car OR airplane

