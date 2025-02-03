# class Payment:
#     def process_payment(self, amount):
#         raise NotImplementedError("Subclasses should implement this method")

# class CreditCardPayment(Payment):
#     def process_payment(self, amount):
#         print(f"Processing credit card payment of {amount}")

# class PayPalPayment(Payment):
#     def process_payment(self, amount):
#         print(f"Processing PayPal payment of {amount}")

# class BitcoinPayment(Payment):
#     def process_payment(self, amount):
#         print(f"Processing Bitcoin payment of {amount}")

# # Example usage:
# payments =CreditCardPayment(100)
# payments=PayPalPayment(100)
# payments= BitcoinPayment(100)

class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses should implement this method")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Bitcoin payment of {amount}")

# Example usage:
credit_card = CreditCardPayment()
credit_card.process_payment(100)

paypal = PayPalPayment()
paypal.process_payment(100)

bitcoin = BitcoinPayment()
bitcoin.process_payment(100)
