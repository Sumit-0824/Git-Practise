#Single inheritence

class A:
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m2(self):
        print("This is m2 method from class B")


bobj=B()
bobj.m1()  #This is m1 method from class A
bobj.m2()  #This is m2 method from class B

#Example 2
class A:
    X,Y=10,20
    def m1(self):
        print(self.X+self.Y)

class B(A):
    a,b=200,100
    def m2(self):
        print(self.a-self.b)

bobj=B()
bobj.m1() #30
bobj.m2() #100