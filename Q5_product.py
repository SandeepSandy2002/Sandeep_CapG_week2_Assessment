class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def display_details(self):
        while True:
            self.quantity=int(input('enter the quantity'))

            if self.stock>self.quantity:
                return f'{self.quantity} stock is available'
            else:
                return f'{self.quantity} stock is not available' 

name=input('enter the name of the item: ')
price=input('enter the price: ')
stock=int(input('enter the stock'))
obj=Product(name,price,stock)
print(obj.display_details())