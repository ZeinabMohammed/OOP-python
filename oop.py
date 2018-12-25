#oop python
class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.fname = first
        self.last= last
        self.pay = pay
        self.email = first +"_" + last + '@company.com'

        Employee.num_of_emps += 1

    def full_name(self):
        return('{} {}'.format(self.fname, self.last))
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        fname, last, pay = emp_str.split('-')
        return cls(fname, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
emp_1 = Employee('zeinab', 'mohammed' , 50000)
emp_2 = Employee('Emad', 'Mostafa', 2500)
emp_str_1 = 'john-jan-2000'
emp_str_2 = 'zoba-emad-3000'
import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

new_emp = Employee.from_string(emp_str_2)
print (new_emp.email)
