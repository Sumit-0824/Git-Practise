class A:
    def m1(self):
        print("This is m1 method from class A")
class B(A):
    def m1(self):
        print("This is m1 method from class B")  #ist
        super().m1()


bobj=B()
bobj.m1()  #This is m1 method from class B
           #This is m1 method from class A



class A:
    a,b=10,20
class B(A):
    i,j=100,200
    def m(self,X,Y):
        print(X+Y)           #3000
        print(self.i+self.j) #300
        print(self.a+self.b) #30


bobj=B()
bobj.m(1000,2000)


#Overriding variables
class Parent:
    name="Scott"

class child(Parent):
    name="John"    #Overiding the variable value

cobj=child()
print(cobj.name)

