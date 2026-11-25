'''
FUNCTION: IT IS NAMED MEMORY BLOCK WHERE WE GOING TO STORE
SOME SET OF INSTRUCTION WHICH ARE MENT TO PERFORM SOME SPECIFIC TASK

use of the function is code reusable

2 types:
1. In-built function:it is function whose task is pre-defined by the developer we can easily
access it ,but we can't modify it
ex: input(),len(),sorted(),range()......

2.User defined function:which will be created based on the user requirement
syntax:
def func_name(args):
    statement blocks

    return values

func_name(args)  # function call

def: it is keyword which is used define a function
func_name : it is a name given to the function to identify its operation
    * to give func name we should follow the identifier rule
return : it is keyword ,to return some value to function
arguments : value/variable used in function

BASED ON THE ARUGUMENTS AND RETURN VALUE USER DEFINED FUNCTION GET CLASSIFIED INTO 4 TYPE
1. Function without argument and without return value
2. Function with argument and without return value
3. Function without argument and with return value
4. Function with argument and with return value
'''
#1. Function without argument and without return value
def greet():
    print('hello world')

#print(greet)   #no output
#greet()         #hello world

# def add():
#     a = int(input('enter the value'))
#     b = int(input('enter the value'))
#     print(a+b)
#
# mul the 3 number

#2. Function with argument and without return value
def mul(a,b,c):
    print(a*b*c)

mul(3,4,5)

#3. Function without argument and with return value
#If we are giving return we need to print to call the function
def add():
    a = int(input('enter the value'))
    b = int(input('enter the value'))
    return a+b

#print(add())    #30
#4.Function with argument and with return value
def sub(a,b):
    return a-b

print(sub(20,10))    #10

# ---------------------------------------------------------------------------------

# WAPT return length of collection
# len()
def length(coll):
    count = 0
    for i in coll:
        count+=1
    return count
print(length([12,34,56,78,90]))  #5
print(length('python'))          #6
print(length({'a':3,'b':6}))     #2

#WPAT check palindrome or not
# s = 'anna'
# s1 = '11211'
# s2 = 'python'
def pali(s):
    if s == s[::-1]:
       print('palindrome')
    else:
        print('not a palindrome')
pali('anna')
pali('11211')
pali('python')


#2nd method

def palindrome(s):
    if s == s[::-1]:
        return 'palindrome'
    else:
        return ('not a palindrome')
print(palindrome('anna'))
print(palindrome('11211'))
print(palindrome('python'))
