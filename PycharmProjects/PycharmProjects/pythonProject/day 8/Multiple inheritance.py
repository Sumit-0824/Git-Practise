class A:
    X,Y=10,20
    def m1(self):
        print(self.X+self.Y)

class B:
    a,b=200,100
    def m2(self):
        print(self.a-self.b)

class C(A,B):
    i,j=5,2
    def m3(self):
        print(self.i*self.j)

cobj=C()
cobj.m1() #30
cobj.m2() #100
cobj.m3() #10
