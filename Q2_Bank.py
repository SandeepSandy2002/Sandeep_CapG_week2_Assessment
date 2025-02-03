'''2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.'''
class BankAccount:
    def __init__(self):
        self.balance=0
        print('please insert your card:')
        self.menu()
# Method to display the menu and perform actions
    def menu(self):
        while True:
            choice=int(input('enter the choice: \n1.deposit \n2.withdrawl \n3.Exit \n'))
            if choice==1:
                self.deposit()
            elif choice==2:
                self.withdrawl()
            elif choice==4:
                print('Invalid option select a valid option')
            elif choice==3:
                print('exited successfully please remove your card')
                break
 # Method to deposit money
    def deposit(self):
        money_deposit=int(input('enter the money to be deposited: '))
        self.balance += money_deposit
        print(f'The {money_deposit} amount is deposited\n The available balance is {self.balance}')
 # Method to withdraw money
    def withdrawl(self):
            money_withdrawl=int(input('enter the money to withdrawl: '))
            if money_withdrawl<=self.balance:
                self.balance-=money_withdrawl
                print(f'The {money_withdrawl} amount is withdrawled\n The available balance is {self.balance}')
            else:
                print('Insufficient Balance')
# Create an object of the BankAccount class
obj=BankAccount()



