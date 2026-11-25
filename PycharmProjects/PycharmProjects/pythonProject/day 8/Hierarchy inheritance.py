class A:
    X,Y=10,20
    def m1(self):
        print(self.X+self.Y)

class B(A):
    a,b=200,100
    def m2(self):
        print(self.a-self.b)

class C(A):
    i,j=5,2
    def m3(self):
        print(self.i*self.j)

bobj=B()
bobj.m1() #30
bobj.m2() #100

cobj=C()
cobj.m1()  #30
cobj.m3()  #10