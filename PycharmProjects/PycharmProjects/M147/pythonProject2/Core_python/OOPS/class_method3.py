'''
In class we can store 3 types of methods
1.Object method
2.Class method
3.Static method

1. object method :-
object method is a method is used to access and modify the members of object.
for all the object methods passing self is mandatory to store the address of object.
If we are calling an object method by using class then we have to pass the address of object.
If we are calling a object method with respect to object then no need to pass the address of object,by default the self will take the respective address of an object

2.Class method :-
Class method is a method which is used to access and modify the members of class.
For all the class methods we have to decorate with “@classmethod”
For all the class method passing  “cls” is mandatory to store the address of class.

3.Static method :-
Static method is a method which is neither belongs to class nor belongs to object but will act as supportive method for class and object.
To create any static method we have to use a decorator called @staticmethod
Since staticmethod is neither belongs to class nor belongs object passing cls or self to store the address is not required.


'''
# company  ,3 c_mem, 2 obj , 5 o_mem
class Company:
    cname = 'apple'
    loc = 'california'
    ceo = 'steve jobs'

    def __init__(self,ename,phno,eid,gmail,pay):
        self.ename = ename
        self.phno = phno
        self.eid = eid
        self.gmail = gmail
        self.pay = pay

    #1.object method
    def display(self):
        return self.eid,self.ename,self.phno,self.gmail,self.pay
    #1.object method to modify/update
    def ch_phno(self,new_phno):
        self.phno = new_phno

    def ch_gmail(self, new_gmail):
        self.gmail = new_gmail

    #2. class method
    @classmethod
    def c_dispaly(cls):
        return cls.cname,cls.loc,cls.ceo
    #class method to modify-
    @classmethod
    def ch_loc(cls, new):
        cls.loc = new
    #3.Static method
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def greet():
        return 'hello '

e1 = Company('john',9988776655,'APP001','john@001.com',20000)
e2 = Company('bill',5566778899,'APP002','bill@002.com',25000)

print(e1.eid,e1.ename,e1.phno,e1.gmail,e1.pay)
print(e2.eid,e2.ename,e2.phno,e2.gmail,e2.pay)

# classname.method name(obj)
print(Company.display(e1))
# objname.methodname()
print(e2.display())
#obj method to call
e1.ch_phno(6360998877)
print(e1.display())


e2.ch_gmail('billi@002.com')
print(e2.display())             #('APP002', 'bill', 5566778899, 'billi@002.com', 25000)
#class method to call
print(Company.c_dispaly())      #('apple', 'california', 'steve jobs')
Company.loc = 'pune'
#static method
print(e1.add(3,4))  #7
print(e1.greet())         #hello