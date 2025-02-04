'''


•	17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.

'''

from abc import ABC, abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass 
    @abstractmethod
    def update(self):
        pass 
    @abstractmethod
    def delete(self):
        pass 
class SQLDatabase(IDatabaseOperations):
    def insert(self,data):
        print('data inserted into database',data)
    def update(self,data):
        print('data updated in database',data)
    def delete(self,data):
        print('data deleted in database',data)
class NOSQLDatabase(IDatabaseOperations):
    def insert(self,data):
        print('data inserted into database',data)
    def update(self,data):
        print('data updated in database',data)
    def delete(self,data):
        print('data deleted in database',data)
sqldatabase=SQLDatabase()
nosqldatabase=SQLDatabase()
sqldatabase.insert([1,2,3])
nosqldatabase.insert([1,2,3])
sqldatabase.update([1,2,3])
nosqldatabase.update([1,2,3])
sqldatabase.delete([1,2,3])
nosqldatabase.delete([1,2,3])