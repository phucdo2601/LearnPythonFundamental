

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
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, email, pay = emp_str.split('-')
        return cls(first, last, email, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        
        return True

emp_1 = Employee('Phuc', 'Do Ngoc', 'testEmailb01@gmail.com', 12313)
emp_2 = Employee('Test-First-02', 'Test-Last-02', 'testEmailb02@gmail.com', 53534)


# print(Employee.fullName(emp_1))

# emp_1.apply_raise()
# Employee.apply_raise(emp_1)

# print(emp_1.pay)

# Employee.apply_raise(emp_2)
# print(emp_2.pay)

# Print instance object

# Employee.set_raise_amount(1.05)

# print(emp_1.__dict__)
# # emp_1.raise_amount = 2.8

# print(Employee.raise_amount)

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print("Number of employees: ",Employee.num_of_emps)

emp_str_1 = 'testFirstName01-testLastName01-testEmail01@gmail.com-42342'
emp_str_2 = 'testFirstName02-testLastName02-testEmail02@gmail.com-42342'
emp_str_3 = 'testFirstName03-testLastName03-testEmail03@gmail.com-42342'

# first_name, last_name, email, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first_name, last_name, email, pay)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.__dict__)
print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2023, 7, 11)

print(Employee.is_workday(my_date))