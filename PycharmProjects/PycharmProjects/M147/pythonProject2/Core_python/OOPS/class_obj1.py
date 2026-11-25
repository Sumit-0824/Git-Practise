""
# OBJECT ORIENTED PROGROMMING
# upto here we are writing program by using functions and control statements and
# datatypes(pre-defined class) .

print(type('hi'))
print(type([]))
l = enumerate([2,3,4])
print(type(l))
'''
<class 'str'>
<class 'list'>
<class 'enumerate'>
'''

# There is another way we can design our program using object, that is we can
# combine data & it functionality and we can rapid inside something called as
# object this called as object oriented programming Technique

# oop’s is way to create a user defined class or datatypes in python
# we can use this technic when ever we want write large programs &
# when ever we deal with real time object we make use of oop’s.
# The major principles(components) of oops are:-
# class , object, inheritance, polymorphism, abstraction and encapsulation.

# -----------------------------------------------------------------------------------
# class : Class is a blue print which is consist of properties & functionalities
# or states and behaviors of real time entity/object. OR
# Class is a  structure  which is used to store the data &which will tell user ,
# how to utilize the stored data. OR
# Class is a set/collection of methods/functions that carry out various operations on instance/data.

# Here two types of class :
# Inbuilt class : It is a pre-defined class with pre-defined method in it.

# user defined class : It is class which is created by user based on their requirements
# syntax
# class classname:
#     properties and
#     functionalities

# while writing the class name we should follow the naming convention i.e,
# the first character of each world should be capital [pascal case]

class MyClass:
    pass

class Points:
    a = 67
    b = 34
    c = 55

# Object / Instances
# Object is an instance of class
# Object is a real time entity (variable) which is created for a particular class.
# We can create any number of object using class.
# synatx:
# obj_name = classname(args)
# creating  the class
class Points:
    a = 67
    b = 34
    c = 55
# create a object
P1 = Points()
P2 = Points()
# create a object member
P1.d = 78
# To access:-
# classname.propertyname
print(Points.a,Points.b,Points.c)   #67 34 55
# objectname.propertyname
print(P1.a,P1.b,P1.c,P1.d) #67 34 55 78
print(P2.a,P2.b,P2.c)      #67 34 55
# To modify:-
# classname.propertyname = new_value
#If we modify the class it will update the class and object
Points.b = 90
print(Points.a,Points.b,Points.c) #67 90 55
print(P1.a,P1.b,P1.c)             #67 90 55
print(P2.a,P2.b,P2.c)             #67 90 55
# objectname.propertyname = new_value
#If we modify the object it will modify only object
P2.c = 88
print(Points.a,Points.b,Points.c)  #67 90 55
print(P1.a,P1.b,P1.c)              #67 90 55
print(P2.a,P2.b,P2.c)              #67 90 88



# ------------------------------------------------------------------------------------
## Example 1
class School:
    sc_name = 'sjs'
    sc_loc = 'pune'
    sc_pric = 'abc'

s1 = School()
s1.std_name = 'steve'
s1.phno = 9988776655

s2 = School()
s2.std_name = 'anna'
s2.phno = 6677889955
s3 = School()

# -------------------------------------------------------------------------------
#Example 2
# Bank , 3 class_mem , 3object, 4-obj_men

class Bank:
    #Class Member
    bname = 'SBI'
    loc = 'Dehli'
    ceo = 'john'
    ifsc = 'SBi678'

c1 = Bank()
#Object member
c1.name = 'mark'
c1.accno = 23456789456
c1.phno = 9988776655
c1.balance = 20000

c2 = Bank()
c2.name = 'bill'
c2.accno = 2345670987
c2.phno = 9984455655
c2.balance = 34000

c3 = Bank()
c3.name = 'steve'
c3.accno = 2349876567
c3.phno = 9988776677
c3.balance = 70000


'''

67 34 55
67 34 55 78
67 34 55
67 90 55
67 90 55
67 90 55
67 90 55
67 90 55
67 90 88

'''
#Compressing the code by removing the common obj using function

# __init__ is method is used to initialize the members of object.
# It is not required to call init method outside the class (in the process of object creation,init method will get invoke by default )
# For __init__ method we need to pass ‘self’ as on argument to store the address of on object, we can pass ony other variable to store the address of on object but according to industrial standard passing self is mandatory.
# In the process of object creation no need to pass the address for self by default self will take the address of an object to which we are initializing the members.

# Bank , 3 class_mem , 3object, 4-obj_men
class Bank:
    bname = 'SBI'
    loc = 'Dehli'
    ceo = 'john'
    ifsc = 'SBi678'

    def c_dit(self, name, accno, phno, balance):
        self.name = name
        self.accno = accno
        self.phno = phno
        self.balance = balance

Bank.c_dit(c1,'mark',23456789456,9988776655,20000)
Bank.c_dit(c2, 'bill',2345670987,9984455655,34000)
Bank.c_dit(c3,'steve',2349876567,9988776677,70000)


###################For compressing it further#########################

class Bank:
    bname = 'SBI'
    loc = 'Dehli'
    ceo = 'john'
    ifsc = 'SBi678'

    def __init__(self, name, accno, phno, balance):
        self.name = name
        self.accno = accno
        self.phno = phno
        self.balance = balance
c1 = Bank('mark',23456789456,9988776655,20000)
c2 = Bank('bill',2345670987,9984455655,34000)
c3 = Bank('steve',2349876567,9988776677,70000)

print(c1.name,c1.accno)
########Rempved after compressed########################
# Bank.c_dit(c1,'mark',23456789456,9988776655,20000)
# Bank.c_dit(c2, 'bill',2345670987,9984455655,34000)
# Bank.c_dit(c3,'steve',2349876567,9988776677,70000)


# c1 = Bank()
# c1.name = 'mark'
# c1.accno = 23456789456
# c1.phno = 9988776655
# c1.balance = 20000
#
# c2 = Bank()
# c2.name = 'bill'
# c2.accno = 2345670987
# c2.phno = 9984455655
# c2.balance = 34000
#
# c3 = Bank()
# c3.name = 'steve'
# c3.accno = 2349876567
# c3.phno = 9988776677
# c3.balance = 70000
'''
