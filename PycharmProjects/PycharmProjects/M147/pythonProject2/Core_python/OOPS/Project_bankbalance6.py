class BankAccount:

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


c1 = BankAccount('steve',10000)
c2 = BankAccount('bill',20000)
#obj.methodname-to call or classname.methodname(obj)
c1.deposit(1000)
c1.transfer(c2,2000)
c2.withdraw(4000)
c2.transfer(c1,1000)
print(c1.transaction)
print(c2.transaction)
c1.statement()
c2.statement()

'''
['Amount Deposit : 1000', 'Amount transfer : 2000', 'Amount Deposit : 1000']
['Amount Deposit : 2000', 'Amount Withdraw : 4000', 'Amount transfer : 1000']
Amount Deposit : 1000
Amount transfer : 2000
Amount Deposit : 1000
------------------------------
the total available balance :10000
Amount Deposit : 2000
Amount Withdraw : 4000
Amount transfer : 1000
------------------------------
the total available balance :17000
'''