'''
•	20. Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.
'''


from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod 
    def login(self):
        pass 
    @abstractmethod 
    def logout(self):
        pass 
    
    
class Google_Auth(UserAuthentication):
    def __init__(self):
        self.username='user'
        self.password='password'
    def login(self,username,password):
        if(username==self.username and password==self.password):
            print('login succcessful')
        else:
            print('invalid username and password')
    def logout(self):
        print('logged out')
        
class Facebook_Auth(UserAuthentication):
    def __init__(self):
        self.username='user'
        self.password='password'
    def login(self,username,password):
        if(username==self.username and password==self.password):
            print('login succcessful')
        else:
            print('invalid username and password')
    def logout(self):
        print('logged out')
        
obj=Google_Auth()
obj.login('user0','password')

obj.login('user','password')
obj.logout()


obj=Facebook_Auth()
obj.login('user','password')
obj.logout()