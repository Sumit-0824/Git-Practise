# inheritance:is a phenomenon of deriving the properties from one class
# # to another class. or
#  Inheritance is a mechanism for creating a new class that specializes
#  or modifies the behavior of the existing class.
# In this case the class from which we inherit the properties is called
# as parent class or super class or base class.
# -The class to which we inherit property is called as child class or
# sub class or derived class.

# class A:
#     pass
# class B(A):
#     pass

class Demo:
    def __init__(self,value):
        self.value = value
    def apple(self):
        print('executing the apple method in Demo')

    def google(self):
        print('executing the google method in Demo')
        print(self.value)

d = Demo(2)
'''
constructor chaining
It is a phenomenon of invoking the constructor of parent class by being there in constructor of child class.
By using this we can reduce the no. of instruction taken to initialize the members of object, which is already done.
There are 3 syntax to perform chaining
1.super( ).__init__(args)
2.super(childname,self).__init__(args)
3.parent.__init__(self,args)

'''
# case1: child inherit from the parent class and child has its oun attribute
class Demo1(Demo):
    def __init__(self,value):
        super().__init__(value)
        #     super() -> used to access the parent class attribute

    def yahoo(self):
        print('executing the yahoo method in Demo1')

# d1 = Demo1()

# case2:child overriding parent class attribute

class Demo2(Demo):
    def apple(self):
        print('executing apple method in Demo2')

d2 = Demo2(34)
'''
method chaining:
It is phenomenon of invoking the method of parent class by being their in child class.
Syntax
Super().mname(args)'''
# case3: child overriding parent class attribute, but reuse the original attribute

class Demo3(Demo):
    def __init__(self,a,b,value):
        super().__init__(value)
        self.a = a
        self.b = b
    def apple(self):
        print(self.value)
        super().apple()
d3 =  Demo3(2,3,89)
