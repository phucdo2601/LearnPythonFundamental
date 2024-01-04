

class Employee:
    def __init__(self, first_name, last_name, email, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = email
    
    def fullName(self):
        # return self.first_name + ' ' + self.last_name
        return '{} {}'.format(self.first_name, self.last_name)

emp_1 = Employee('Phuc', 'Do Ngoc', 'testEmailb01@gmail.com', 12313)


print(emp_1.fullName())

print(Employee.fullName(emp_1))