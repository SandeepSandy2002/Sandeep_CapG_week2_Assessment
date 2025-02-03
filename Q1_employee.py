'''. Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.'''
##APPROACH 1
class Employee:
    def __init__(self):
        self.name=input('enter the name: ')
        self.id=int(input('enter the employee id:'))
        self.department=input('enter the department: ')
e1=Employee()
print(e1.name)
print(e1.id)
print(e1.department)
##APPROACH 2

class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department

name=input('enter the name: ')
id=int(input('enter the empolyee id:'))
department=input('enter the department')

e1=Employee(name,id,department)
print(e1.name)
print(e1.id)
print(e1.department)