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
    def __repr__(self):
        return "Employee('{},{},{}')".format(self.first, self.last, self.pay)
    def __str__(self):
        return '{}, {}'.format(self.full_name(), self.email)
    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.full_name())
emp_1 = Employee('zeinab', 'mohammed' , 50000 )
emp_2 = Employee('zeinab', 'mohammed' , 20000 )
print ('test'.__len__())
print (len(emp_1))

#print (emp_1)
#print repr(emp_1.__repr__())
#print str(emp_1)
print (str.__add__('a','d'))
