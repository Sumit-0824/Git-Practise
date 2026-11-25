# Polymorphism:it refers to method /function/operator  with the same name that can be
#  executed on many object or class
# 3 ways:
# -operator overloading
# -method overloading
# -method overriding


# operator overloading:it is phenomenon of making the operator to work on the object of
# # user defined datatype/class by invoking the respective magic method
# if we try to acess directly by __add__(self)----it will throw error. to access we need to create as below
class Points:
    a = 98
    def __add__(self, other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a
    def __mul__(self, other):
        return self.a*other.a
p1 = Points()
p2 = Points()
print(p1+p2)
print(p1-p2)
print(p1*p2)
# print(dir(p1))

# -method overloading:a class having  more than one method with same name but
# diffrent formal arguments
#In python method overloading does not support

# def add(a,b):
#     return a+b
# def add(a,b,c):
#     return a+b+c
# def add(a,b,c,d):
#     return a+b+c+d
#
# add(3,4,5)
# add(3,4)

# -method overriding:the process of providing  the new implementation to the superclass
# # method from the subclass.

class BankAccount:
    INTEREST_RATE = 0.05

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction = []

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('amount should be greater than 0')
        self.balance = self.balance + amount
        self.transaction.append(f'Amount Deposit : {amount}')

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('insufficient funds')
        self.balance = self.balance - amount
        self.transaction.append(f'Amount Withdraw : {amount}')

    def transfer(self, to_account, amount):
        if amount > self.balance:
            raise ValueError('insufficient funds')
        self.balance -= amount
        to_account.deposit(amount)
        self.transaction.append(f'Amount transfer : {amount}')

    def statement(self):
        for item in self.transaction:
            print(item)
        print('-' * 30)
        print(f'the total available balance :{self.balance}')

    def roi(self):
        interest_amount = self.balance * BankAccount.INTEREST_RATE
        self.balance += interest_amount
        self.transaction.append(f'Interest amount credited: {interest_amount}')


class SavingBankAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def withdraw(self, amount):    #Overiding the parent class function
        if amount > 10000:
            raise ValueError('max withdraw limit 10k')
        super().withdraw(amount)
