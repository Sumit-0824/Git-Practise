########Class Assignment###########

# # a=10
# # b=20
# # def func():
# #     res = a + b   #Wrong way of writing code,this line is outside above the local variable
# #     a=200
# #     b=300
# #     return res
# # print(func())
# #
#
#
# #
# # a=10
# # b=20
# # def func():
# #     a=200
# #     b=300
# #     res= a+b
# #     return res
# # print(func()) #500
#
# # a=40
# # b=70
# # def func():
# #     a=4
# #     b=5
# #     print(a+b)
# # func()
# # print(a+b)
#
# a=10
# b=20
# def func():
#     global a
#     print(a)
#     a+=1
#     print(a)
#     a=1.3
#     print(a)
# func()
# print(a+5)
# print(a+b)

#Once modified we cannot access the original value
#####class Notes###########

# VARIABLE SCOPE :The scope of a variable in python is depends on the
# place where the value for the variable is assigned in your source code
# variables assigned inside a function do not clash with variables outside the function,
# even if the same variable names are used elsewhere.

# LEGB : Local ,Enclosing , Global and Built-in
#
# Global :Global variable are the variable which gets created inside main space.

# We can access and modify global variable inside the main space in the
# same way we can access global variables but can’t modify at method area or function area.

# a = 78 # Global variable
# def func():
#     # a = a+7  # We can't modify the global variable inside
#     print(a)
# func()
# print(a)
#
# a = a+4  # modification
# # c = a+4  # oprating and assg
# print(a)

 # local variable:Local variables are the variables ,which will get created
# inside method area or function area.
# We can access and modify local variables inside the same function, but it
# can't be accessed outside the function

def func():
    a =78 # local variable
    a += 5  #a=a+5
    print(a)
func()

# print(a)
# LEGB
a = 20
b = 60
def func():
    a = 100
    b = 200
    return a+b
print(func()) #300 If a in local variable not available then it will check in global --20+200--220
print(a+b)    #80

def func():
    return a+10
print(func())

# a = 10
# b =20
# def func():
#     res = a+b   # we cant write above the assignment
#     a = 200
#     b = 300
#     return res
# print(func())

a = 10
b =20
def func():
    a = 200
    b = 300
    res = a + b
    return res
print(func())

# a = 10
# b =20
# def func():
#     a = a+1     # WE cannot modify the global variable
#     b = b+1
#     return a+b
# print(func())

a = 40
b = 70
def func():
    a = 4
    b = 5
    print(a+b)
func()            #9
print(a+b)        #110


# We can’t modify global variable inside the method area directly, to modify global variable
# inside the method area we should use global keyword and global keyword should be
# first instruction.

a = 10
b =20
def func():
    global a,b
    a = a+1
    b = b+1
    return a+b
print(func()) #32
a = 10
b = 20
def func():
    global a
    print(a+b) #30
    print(a)   #10
    a += 1
    print(a)    #11
    a = 1.3
    print(a)     #11.3

func()           #1.3
print(a+5)       #6.3

# ----------------------------------------------------------------------------

# Enclosing / Non Local Variable:
# Non-local space are those which are neither global nor local
# If a nested function has to be access and modify the variable of outer function ,we use non-local keyword

# LEGB
x = 78  # Global variable
def func():
    x = 86  # non local variable
    def inner():
        x = 56  # local variable
        print(x)
    return inner()
func()   #56
func()   # 86 if local variable is disabled
func()   # 78 if local and non local variable is disabled

#Built-in
from math import *
# pi = 3.1456  # global
def func():
    # pi = 3.14   # nonlacal
    def inner():
        # pi = 3.142567  #local
        print(pi)
    return inner()
func()















