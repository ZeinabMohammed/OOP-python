#oop python
class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last= last
        self.pay = pay
        self.email = first +"_" + last + '@company.com'

    def full_name(self):
        return('{} {}'.format(self.first, self.last))
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
class Developer(Employee):
    raise_amount=1.10
    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp  in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('==> ' + emp.full_name())
dev_1 = Developer('zeinab', 'mohammed' , 50000, 'python')
dev_2 = Developer('Emad', 'Mostafa', 2500, 'java')
mgr_1 = manager('suz', 'ahm', 2100, [dev_1])
mgr_2 = manager('suz', 'ahm', 2100, [])
repr(dev_1)
str(dev_1)

"""
print(dev_1.prog_lang)
(dev_1.apply_raise())
print(dev_1.pay)
print (dev_2.prog_lang)"""
