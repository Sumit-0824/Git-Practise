i,j=15,25 # global variables
class Myclass:
    a,b=10,20 #class variables
    def add(self,X,Y): #local variables
        print(X+Y)             #X,Y are local variables #300
        print(self.a+self.b)   #a,b are class variables #30
        print(i+j)             #i,j are global variables #40

mc=Myclass()
mc.add(100,200)