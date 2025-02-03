class person:
    def __init__(self):
        self.workdays=150
class employee(person):
    def __init__(self):
        super().__init__()
        self.present_days=100
class Manager(employee):
     def __init__(self):
        super().__init__()
     def approve_leave(self):
         if (ob3.present_days/ob3.workdays)*100 < 90:
             print('leave rejected')
         else:
             print('leave approved')
        
ob1=employee()
print(f'total work days {ob1.workdays}')
print(f'total present {ob1.present_days}')
ob3=Manager()
print(ob3.workdays)
print(ob3.present_days)
ob3.approve_leave()



