#super
# class Parent():
#     def greet(self):
#         return "Hello from Parent"
#
# class Child(Parent):
#     def greet(self):
#         return super().greet()+"Hello from child"
# c=Child()
# #c.hellogreet()
# c.greet()


#Constructor

class Parent():
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def __init__(self,title):            #defalt constructor if it has only self but if we add any argument then it is parametrised
      self.title=title                   # to make it global
    def greet(self):
        return super().greet()+"Hello from child"+self.title       #Title can be accessed with self
c=Child("Rahul shetty academy")  #Pass the title ie parameter
#c.hellogreet()
c.greet()

