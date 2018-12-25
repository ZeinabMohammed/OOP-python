#oop python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last= last
        self.pay = pay
    @property
    def email(self):
        return('{}.{}@email.com'.format(self.first, self.last))
    @property
    def full_name(self):
        return('{} {}'.format(self.first, self.last))
    @fullname.setter
    def fullname(self, name):
        first, last=name.split(' ')
        self.first = first
        self.last = last
emp_1 = Employee('zeinab', 'mohammed' , 50000)
emp_2 = Employee('Emad', 'Mostafa', 2500)
emp_1.full_name = 'corey chefer'
print(emp_1.first)
print (emp_1.full_name)
print (emp_1.email)
