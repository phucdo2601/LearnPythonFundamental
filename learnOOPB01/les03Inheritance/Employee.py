

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
    
class Developer(Employee):
    raise_amount = 5 
    
    def __init__(self, first_name, last_name, email, pay, pro_lang):
        super().__init__(first_name, last_name, email, pay)
        self.pro_lang = pro_lang
        
class Manager(Employee):
    
    def __init__(self, first_name, last_name, email, pay, employees=None):
        super().__init__(first_name, last_name, email, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for employee in self.employees:
            print('--->', employee.fullName())

dev_1 = Developer('Phuc', 'Do Ngoc', 'testEmailb01@gmail.com', 12313, 'python')
dev_2 = Developer('Test-First-02', 'Test-Last-02', 'testEmailb02@gmail.com', 53534, 'Java')

mgn_1 = Manager('Test-mgn-First-02', 'Test-mgn-Last-02', 'testEmailMgnb02@gmail.com', 53534, [dev_1, dev_2])


# print(help(Developer))
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.__dict__)

mgn_1.print_employees()