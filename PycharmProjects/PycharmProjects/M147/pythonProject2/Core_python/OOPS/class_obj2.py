#Constructor
# __init__ is method is used to initialize the members of object.
# It is not required to call init method outside the class (in the process of object creation,init method will get invoke by default )
# For __init__ method we need to pass ‘self’ as on argument to store the address of on object, we can pass ony other variable to store the address of on object but according to industrial standard passing self is mandatory.
# In the process of object creation no need to pass the address for self by default self will take the address of an object to which we are initializing the members.


#Ex-1
class MyClass:
    def __init__(self):
        print(f'hello')

m1 = MyClass()    #hello
m2 = MyClass()    #hello


#EX-2
class MyClass:
    def __init__(self,name):
        print(f'hello {name}')

m1 = MyClass('steve')  #hello steve
m2 = MyClass('anna')   #hello anna


#Company,3_cls Mem,2 obj,5 obj_mem

class Company:
    #Class Member
    cname = 'TCS'
    loc = 'Bangalore'
    ceo = 'Satya'
    #As per industry standard we need to do self instead of object
    def __init__(self,name,empid):
        #Object.args
        self.name=name
        self.empid=empid
#Object member
c1=Company('john','TCS001')
c2=Company('Mark','TCS002')
c3=Company('Livin','TCS003')
c4=Company('Miller','TCS004')
c5=Company('David','TCS005')
#
print(c1.name,c1.empid)
print(c2.name,c1.empid)
print(c3.name,c1.empid)
print(c4.name,c1.empid)
print(c5.name,c1.empid)

'''
Output
john TCS001
Mark TCS001
Livin TCS001
Miller TCS001
David TCS001
'''
