'''
Let see some error which some in our daily programs

SyntaxError:This exception is raised when misspelled the keyword, a missing colon or an
unbalanced parenthesis

ValueError:This exception is raised when a function or method is called with an invalid
argument or input ,such as trying to convert a string to an integer when the string does not represent a valid integer.

TypeError:This exception is raised when  an operation or function is applied to an object
of the wrong type , such as adding a string to a integer

IndexError :

KeyError:

ImportError:

NameError:

AttributeError:

ZeroDivisionError:

'''
# EXCEPTION
# It is a process of responding to unwanted or unexpected event when it is runs
# exception handling deals with these events to avoid the program or system crashing and
# without this process, exception would disturb the normal operation

# Exception can be handled by the using try and except keyword.
# -try :- is going to have the problem statement and
# -except :- for the solution for above problem statement.It executes only when exception occured
# -finally :- finally is a default block which will get execute if the program is having any error if the programs not having any error
#-else :-executes only exceptions not occured
# syntax
'''
try:
    statement block
except:
    statement block
else:
    statement block
finally:
    statements    

'''
# -Exception can be handled in 3 ways.
# 1. specific exception handling
# 2. generic exception handling
# 3. default exception handling

# 1. specific exception handling:
# try:
#     statement block
# except error_name:
#     statement block
# else:
#     statement block
# finally:
#     statements
# while True:
#     +
#         age = int(input('enter the age:'))
#         num = int(input('enter the value'))
#         print(age/num)
#         break
#     except ValueError:
#         print('enter the number only')
#     except ZeroDivisionError:
#         print('enter more than 0')

names = ['apple','google','yahoo','yahoo','apple','apple']
count ={}
for name in names:
    try:
        count[name]+=1
    except KeyError:
        count[name]  = 1

print(count)

def div(n1,n2):
    try:
        res = n1/n2
        print(res)
    except (TypeError,ZeroDivisionError):
        print('enter the number greaterthan 0')

div(87,8)

# 2. generic exception handling
'''
generic exception handling refers to using a try-except block to catch any kind of exception that may 
arise during the execution of the program. Instead of 
specifying a particular exception type, you can use a general except block that catches all exceptions.
'''
# try:
#     statement block
# except Exception:
#     statement block
# else:
#     statement block
# finally:
#     statements

# while True:
#     try:
#         age = int(input('enter the age:'))
#         num = int(input('enter the value'))
#         print(age/num)
#         break
#     except Exception:
#         print('enter the number greaterthan 0')

# 3. default exception handling
# while True:
#     try:
#         age = int(input('enter the age:'))
#         num = int(input('enter the value'))
#         print(age/num)
#         break
#     except :
#         print('enter the number greaterthan 0')

# --------------------------------------------------------------------------------
# Custom exception : python will support the user to throw the error in the program by
# # their own with the help of raise keyword
# syntax: raise error_name('message')
#Example 1
# mob = input('enter the number:')
# if mob.isdigit() and len(mob)==10:
#     print(mob)
# else:
#     raise ValueError('enter the valid mob number')
#Example 2
# email = input('Enter email id :')
# if '@' in email and email.endswith('.com'):
#     print(email)
# else:
#     raise Exception('Enter valid email id')
#
#Example 3
# age=int(input("Enter age: "))
# if (age>18):
#     print("You can login")
# else:
#     raise Exception("You cannot login as age is not greater than 18")

#------------------------------------------------------------------------------
#Creating own error name
# class errorname(Exception):
#     statement

class MyError(Exception):
    pass

email = input('Enter email id :')
if '@' in email and email.endswith('.com'):
    print(email)
else:
    raise MyError('Enter valid email id')








