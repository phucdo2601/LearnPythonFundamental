

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first_name, last_name, email, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        Employee.email = email
        
        self.num_of_emps += 1
    
    def fullName(self):
        # return self.first_name + ' ' + self.last_name
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Phuc', 'Do Ngoc', 'testEmailb01@gmail.com', 12313)
emp_2 = Employee('Test-First-02', 'Test-Last-02', 'testEmailb02@gmail.com', 53534)


print(emp_1.fullName())

# print(Employee.fullName(emp_1))

# emp_1.apply_raise()
# Employee.apply_raise(emp_1)

# print(emp_1.pay)

# Employee.apply_raise(emp_2)
# print(emp_2.pay)

# Print instance object

print(emp_1.__dict__)
emp_1.raise_amount = 2.8

print(Employee.raise_amount)

print(emp_1.raise_amount)
print(emp_2.raise_amount)

print("Number of employees: ",Employee.num_of_emps)