class MyClass:
    def __init__(self):
       print("This is constructor...")
    def m1(self):
        print("hello...")

    def m2(self,X,Y):
        return (X+Y)


mc=MyClass()
mc.m1()
print(mc.m2(10,20))