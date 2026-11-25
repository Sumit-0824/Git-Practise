#Acessing the class variable
class Myclass:
    a,b=10,20  #class variables
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

mc=Myclass()
mc.add()
mc.mul()