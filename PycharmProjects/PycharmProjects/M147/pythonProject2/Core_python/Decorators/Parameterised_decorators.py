# parameter decorator
#No need to give underscore ,we can give different name
from time import sleep,time
def _delay(time_delay):
    def delay(func):
        def wrapper(*args,**kwargs):
            sleep(time_delay)
            return func(*args,**kwargs)
        return wrapper
    return delay
#
@_delay(3)
def greet():
    return 'hello world'
# @_delay(5)
# def greeting(name):
#     return f'hello {name}'
# @_delay(7)
# def add(a,b):
#     return a+b
# @_delay(7)
# def sub(a,b):
#     return a-b
# @_delay(10)
# def mul(a,b,c):
#     return a*b*c
#
print(greet())             #hello world
print(greet())
print(greet())
print(greet())

# print (greeting('Sumit'))  #hello Sumit
# print(add(3,4))      #7
#print the statement

# #2nd Example
# count = {}
# def _count(func_name):
#     if func_name in count:
#         count[func_name]+=1    # add the no. of repeattion
#     else:
#         count[func_name] = 1   # add the new item to list
#
# def _max_call(val):
#     def max_call(func):
#         def wrapper(*args):
#             _count(func.__name__)
#             if count[func.__name__]>val:
#                 raise ValueError(f'max call exceeds which is {val}')
#             return  func(*args)
#         return wrapper
#     return max_call
#
# @_max_call(3)
# def greet():
#     return 'hello world'
#
# #ValueError: max call exceeds which is 3
# #How we will print the parametrised decorator
#
# print(greet())
# # print(greet())
# # print(greet())
# print(count)  #4th time we will get error
# @_max_call(5)
# def greeting(name):
#     return f'hello {name}'
# @_max_call(7)
# def add(a,b):
#     return a+b
# @_max_call(7)
# def sub(a,b):
#     return a-b
# @_max_call(10)
# def mul(a,b,c):
#     return a*b*c


#iteratable  __iter__   Ex--list,string,tuple,set,dictionary,range
#dir(int)Do not have magic method----__iter__ cannot iterate
#We can check for other data types- list,string,tuple,set,dictionary...
#We can check for inbuilt functions----sum,reverse,zip,enumerate Syntax-dir(sum)

#iterator Magic method----  __iter__,__next__-----Ex--Zip,enumerate,reverse

