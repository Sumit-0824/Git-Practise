# Magic_methods or Dunder method:are the methods starting and ending with double underscores.

# container protocol
# __contains__(self,obj) ---> in
#Will be used by developer not required for tester
class Points:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __contains__(self, item):
        if item == self.a or item == self.b:
            return True
        return False

    def __len__(self):
        return 2

    def __getitem__(self, item):
        if item == 0:
            return self.a
        elif item == 1:
            return self.b
        else:
            raise IndexError('index out of range')

    def __setitem__(self, key, value):
        if key == 0:
            self.a = value
        elif key == 1:
            self.b = value
        else:
            raise IndexError('index out of range')


p1 = Points(3, 6)
p2 = Points(6, 9)

print(3 in p1)
print(len(p1))
print(len(p2))
print(p1[0])
print(p1[1])
p2[0] = 8
print(p2[0])
# print(p1[5])
print(p1.a)


# -----------------------------------------------------------------------------------
# attribute protocol
# __getattribute__
# __getattr__
# __setattr__

class PositivePoints:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, key, value):
        if value < 0:
            raise ValueError()

        super().__setattr__(key, value)


p1 = PositivePoints(3, 6)
p2 = PositivePoints(5, 9)
print(dir(p1))
print(p1.b)
# --------------------------------------------------------------------------
# comparision protocol
'''
__lt__ -lesser than
__gt__- greater than
__eq__- equal to
__le__-less than equal too
__ge__-greater than equal too
__ne__-not equal too
'''


class Employees:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __lt__(self, other):
        if self.age < other.age:
            return True
        return False

    def __gt__(self, other):
        if self.age > other.age:
            return True
        return False

    def __lt__(self, other):
        if self.age == other.age:
            return True
        return False


e1 = Employees('anna', 25, 40000)
e2 = Employees('steve', 34, 50000)
e3 = Employees('john', 30, 40000)
print(dir(e1))
print(e1 > e2)
print(e2 > e3)


class Employees:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __le__(self, other):
        if self.pay <= other.pay:
            return True
        return False

    def __ge__(self, other):
        if self.pay >= other.pay:
            return True
        return False

    def __ne__(self, other):
        if self.pay != other.pay:
            return True
        return False


e1 = Employees('steve', 34, 50000)
e2 = Employees('john', 30, 40000)
# print(e1==e2)


# number protocol
'''
__add__
__sub__
__mul__
__truediv__-->/
__floordiv__-->//
__mod__--> %
__pow__ 
'''


class Points:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __sub__(self, other):
        return self.a - other.a, self.b - other.b

    def __mul__(self, other):
        return self.a * other.a, self.b * other.b

    def __floor__(self, other):
        return self.a // self.b, other.a // other.b


# p1 = Points(3,4)

# --------------------------------------------------------------------------
# function protocol
# __call__

class Greeting:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return f'Hello {self.name}'


greet = Greeting('anna')
print(greet())

# iterator protocol:__iter__,__next__

# object protocol : __new__,__del__,__repr__

# Descriptor : __get__,__set__,__del__

# context manager protocol : __enter__,__exit__






