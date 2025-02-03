'''4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.'''
class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    def display_details(self):
        return f'The student details as follows:\nName:{obj.name}\nRoll_number:{obj.roll_number}'
name=input('enter the name of the student: ')
roll_number=input('enter the rollnumber: ')
obj=Student(name,roll_number)
print(obj.display_details())
