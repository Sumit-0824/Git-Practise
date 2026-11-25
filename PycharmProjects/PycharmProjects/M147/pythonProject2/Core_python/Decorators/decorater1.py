

#Self practice-----------------------------------
#import the module
# Create decorator using the Syntax
'''
def dec_name(func):
    def inner_func(*args,**kwargs):
        features
        return  func(*args,**kwargs)
    return inner_func

@dec_name
def func():
    pass
'''
#Steps
#Create function
#Apply the decorator to the function by using @ dec_name
#Call the function by print(function(arguments)

from time import sleep
#create the decorator
def delay(func):
    def wrapper(*args,**kwargs):
        sleep(5)
        return func(*args,**kwargs)
    return wrapper

# def spam(some_func,*args):
#     print(f'you called {some_func.__name__} function')   #you called mul function
#     return some_func(*args)

def log(some_func):
    def spam(*args,**kwargs):
        print(f'you called {some_func.__name__} function')
        return some_func(*args,**kwargs)
    return spam

@delay
@log
def add(a,b):
    return a+b


@log
def greet():
    return 'hello world'

# apply the decorator
@log
@delay
def mul(a,b,c):
    return a+b+c
#call the function
print(greet())   #1st You called greet function.......hello world
print(add(10,20)) #you called add function......30

# DECORATOR: it is a function which add an extra functionality to the existing function without
#  modifying the original function or existing function
#Class notes--------------------------------------------------------------------------------------
# syntax:
'''
def dec_name(func):
    def inner_func(*args,**kwargs):
        features
        return  func(*args,**kwargs)
    return inner_func

@dec_name
def func():
    pass
'''

def delay(func):
    def wrapper(*args,**kwargs):
        sleep(5)
        return func(*args,**kwargs)
    return wrapper
#Skip this
# a = delay(mul)
# print(a(3,4,6))   # we cannot pass the argument together....we need to pass it separately else it will give error

def log(func):
    def wrapper(*args,**kwargs):
        print(f'you called {func.__name__} function')
        return func(*args,**kwargs)
    return wrapper

# @delay  # greet = delay(greet)
@log
def greet():
    return 'hello world'
@log
def greeting(name):
    return f'hello {name}'
# @log
# def add(a,b):
#     return a+b
#
# @delay
# @log
# def sub(a,b):
#     return a-b
# @delay
# def mul(a,b,c):
#     return a*b*c

print(greet())             #First it will execute the decorator under log then it will execute the greet function Hello World
print(greeting('steve'))   #First it will execute the decorator function then it will execute the greeting function hello steve