a,b=15,25 # global variables
class Myclass:
    a,b=10,20 #class variables
    def add(self,a,b): #local variables
        print(a+b)             #a,b are local variables #300
        print(self.a+self.b)   #a,b are class variables #30
        print(globals()['a']+globals()['b'])             #a,b are global variables #40

mc=Myclass()
mc.add(100,200)
