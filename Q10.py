class Electronics:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def turn_on(self):
        return "Turning on the electronic device"

    def turn_off(self):
        return "Turning off the electronic device"

class MobileDevice(Electronics):
    def __init__(self, brand, price, model):
        super().__init__(brand, price)
        self.model = model

    def make_call(self, number):
        return f"Calling {number} from {self.model}"

    def turn_on(self):
        return f"Turning on the mobile device {self.model}"

class SmartPhone(MobileDevice):
    def __init__(self, brand, price, model, os):
        super().__init__(brand, price, model)
        self.os = os

    def browse_internet(self):
        return "Browsing the internet on the smartphone"

iphone = SmartPhone(brand="Apple", price=79999, model="iPhone 15", os="iOS")

print(iphone.turn_on())
print(iphone.make_call("1234567890"))
print(iphone.browse_internet())
print(iphone.os)
print(iphone.price)
print(iphone.model)
