# ENCAPSULATION:the process of binding both states and behaviour of object together is known as encapsulation
# it is used for data hiding.
# data hiding: the process of restriting the direct access to the states of a class but
# providing controlled access with the help of behaviours of a same class

# - by making the states as private
# - getter and setter
#1. general method
class Bank:
    def __init__(self):
        self.__balance = 30000

# c1=Bank()
# c2=Bank()
# c1.balance=56000
# print(c1.balance) #We cannot modify the balance &it is not visible to all for that
    def getter(self):
        return self.__balance

    # To update the balance from the admin side only
    def setter(self,new):
        self.__balance = new

c1  = Bank()
c2 = Bank()
# c1.balance=56000    # We cannot modify
print(c1.getter())    #30000 It will show only our amount in the our account
c1.setter(56000)      # To update the balance from the admin side only

print(c1.getter())   #56000
# 2.property() function:
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.__grade = grade
    def getter(self):
        return f'{self.name} got this {self.__grade}'
    def setter(self,new_grade):
        self.__grade = new_grade
    msg = property(getter,setter)

s1 = Student('anna','A')
s2 = Student('steve','B')
s1.msg = 'B'
print(s1.msg) #anna got this B

#3. @property
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,new):
        if type(new) == int:
            self.__balance = new
        else:
            raise Exception('enter the valid amount')
c1 = BankAccount(30000)
c1.balance = 90000
print(c1.balance) #90000
