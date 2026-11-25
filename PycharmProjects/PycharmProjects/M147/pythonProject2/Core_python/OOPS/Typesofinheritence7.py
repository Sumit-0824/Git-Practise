# types of inheritance
'''
single level inheritance: it is deriving the properties from single parent class to single child class
class A:
    pass
class B(A):
    pass
'''

class BankAccount:
    INTEREST_RATE = 0.05
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.transaction = []

    def deposit(self,amount):
        if amount<0:
            raise ValueError('amount should be greater than 0')
        self.balance = self.balance+amount
        self.transaction.append(f'Amount Deposit : {amount}')

    def withdraw(self,amount):
        if amount> self.balance:
            raise  ValueError('insufficient funds')
        self.balance = self.balance-amount
        self.transaction.append(f'Amount Withdraw : {amount}')

    def transfer(self,to_account,amount):
        if amount>self.balance:
            raise ValueError('insufficient funds')
        self.balance -= amount
        to_account.deposit(amount)
        self.transaction.append(f'Amount transfer : {amount}')

    def statement(self):
        for item in self.transaction:
            print(item)
        print('-'*30)
        print(f'the total available balance :{self.balance}')

    def roi(self):
        interest_amount = self.balance*BankAccount.INTEREST_RATE
        self.balance+=interest_amount
        self.transaction.append(f'Interest amount credited: {interest_amount}')



c1 = BankAccount('steve',10000)
c2 = BankAccount('bill',20000)
c1.deposit(1000)
c1.transfer(c2,2000)
c2.withdraw(4000)

print(c2.transaction)
c1.statement()
c2.statement()
c1.roi()
c2.transfer(c1,1000)
c1.statement()


class SavingBankAccount(BankAccount):

    def __init__(self,name,balance):
        super().__init__(name,balance)

    def withdraw(self,amount):
        if amount>10000:
            raise ValueError('max withdraw limit 10k')
        super().withdraw(amount)

# multi level : it is process of deriving the properties from one class to another class by
# considering more one level
class A:
    pass
class B(A):
    pass
class C(B):
    pass

class BankAccount:
    INTEREST_RATE = 0.05
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.transaction = []

    def deposit(self,amount):
        if amount<0:
            raise ValueError('amount should be greater than 0')
        self.balance = self.balance+amount
        self.transaction.append(f'Amount Deposit : {amount}')

    def withdraw(self,amount):
        if amount> self.balance:
            raise  ValueError('insufficient funds')
        self.balance = self.balance-amount
        self.transaction.append(f'Amount Withdraw : {amount}')

    def transfer(self,to_account,amount):
        if amount>self.balance:
            raise ValueError('insufficient funds')
        self.balance -= amount
        to_account.deposit(amount)
        self.transaction.append(f'Amount transfer : {amount}')

    def statement(self):
        for item in self.transaction:
            print(item)
        print('-'*30)
        print(f'the total available balance :{self.balance}')

    def roi(self):
        interest_amount = self.balance*BankAccount.INTEREST_RATE
        self.balance+=interest_amount
        self.transaction.append(f'Interest amount credited: {interest_amount}')

class SavingBankAccount(BankAccount):

    def __init__(self,name,balance):
        super().__init__(name,balance)

    def withdraw(self,amount):
        if amount>10000:
            raise ValueError('max withdraw limit 10k')
        super().withdraw(amount)

class SalaryAccount(SavingBankAccount):
    def deposit(self,amount):
        if amount<20000:
            raise ValueError('salary should be greater than 20k')
        super().deposit(amount)


# Hierarchical inheritance:it is process of deriving the properties from
# single parent class to multiple child class
'''
class A:
    pass
class B(A):
    pass
class C(A):
    pass 
'''
class BankAccount:
    INTEREST_RATE = 0.05
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.transaction = []

    def deposit(self,amount):
        if amount<0:
            raise ValueError('amount should be greater than 0')
        self.balance = self.balance+amount
        self.transaction.append(f'Amount Deposit : {amount}')

    def withdraw(self,amount):
        if amount> self.balance:
            raise  ValueError('insufficient funds')
        self.balance = self.balance-amount
        self.transaction.append(f'Amount Withdraw : {amount}')

    def transfer(self,to_account,amount):
        if amount>self.balance:
            raise ValueError('insufficient funds')
        self.balance -= amount
        to_account.deposit(amount)
        self.transaction.append(f'Amount transfer : {amount}')

    def statement(self):
        for item in self.transaction:
            print(item)
        print('-'*30)
        print(f'the total available balance :{self.balance}')

    def roi(self):
        interest_amount = self.balance*BankAccount.INTEREST_RATE
        self.balance+=interest_amount
        self.transaction.append(f'Interest amount credited: {interest_amount}')

class SavingBankAccount(BankAccount):

    def __init__(self,name,balance):
        super().__init__(name,balance)

    def withdraw(self,amount):
        if amount>10000:
            raise ValueError('max withdraw limit 10k')
        super().withdraw(amount)

class SalaryAccount(BankAccount):
    def deposit(self,amount):
        if amount<20000:
            raise ValueError('salary should be greater than 20k')
        super().deposit(amount)

class SeniorcitizenAccount(BankAccount):
    INTEREST_RATE = 0.08