
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @email.setter
    def email(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @email.deleter
    def email(self):
        print('Delete email')
        self.first = None
        self.last = None
    
    def getFirst(self):
        return self.first
    
    def setFirst(self, first):
        self.first = first
        
    def getLast(self):
        return self.last
    
    def setLast(self, last):
        self.last = last
        
emp_1 = Employee('John', 'Smith')
print(emp_1.getFirst())
print(emp_1.fullname())
print(emp_1.email)

emp_1.email = "Phuc do"
print(emp_1.email)
del emp_1.email
