#Positional Arguments
#keyword Arguments
#Ex 1
# def fun(i,j):
#     print(i,j)
# fun(10,20)# Keyword argument

#Ex 2
# def fun(i,j=10):
#     print(i,j)
# fun(100,200) #100,200
# fun(100)          #100,10
#Ex 3 Keyword arguments

def greetings(name,greetmsg):
    print(greetmsg+"  "+name)
greetings(name='John',greetmsg="Hello")
greetings(greetmsg="Hello",name='John',)

#Ex=4
# def my_fun(a,b,c):
#     print(a,b,c)
# my_fun(10,20,30) #Positional aruguments
# my_fun(a=10,b=20,c=30) #Keyword arguments
# my_fun(b=10,a=20,c=30) #Keyword arguments
# #combination of both
# my_fun(10,20,c=30)
# my_fun(10,a=20,c=30)
#my_fun(10,a=20,30) #Incorrect because postional argument must appear before any keyword arguments
#my_fun(10,30,b=20)   #TypeError: my_fun() got multiple values for argument 'a'

#Ex=5 Function can return multiple values
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
largest(100,200)
print(largest(100,200))
print(largest(20,10))

