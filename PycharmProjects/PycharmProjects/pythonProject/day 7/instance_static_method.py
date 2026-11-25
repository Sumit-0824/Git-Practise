class Myclass:
    def m1(self):
        print("This is instance method")

    @staticmethod   #annotation
    def m2(self,num):
        print(self,num)

mc=Myclass()
mc.m1()
#mc.m2(100,200)
Myclass.m2(100,200)#Static method is called using the class