a = 44
b = a

c = [1,2,3,4,4]
d = c

e = {'x':2,'y':5}
f = e

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b,c):
    return a*b*c
y = add

thing = []
thing.append(a)
thing.append(c)
thing.append(f)
thing.append(y)   #  we can append function too

def demo(someting,*args):
    print(someting(*args))

demo(add,5,6)
#print(add(5,6))



def spam(some_func,*args):
    print(f'you called {some_func.__name__} function')   #you called mul function
    return some_func(*args)
print(spam(mul,5,8,9))                             #360

# DECORATOR: it is a function which add an extra functionality to the existing function without
#  modifying the original function or existing function




