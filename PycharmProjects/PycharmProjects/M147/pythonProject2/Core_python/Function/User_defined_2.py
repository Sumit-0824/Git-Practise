#WAPT to create square no in the list
# l=[2,3,4,5,6,9,7]
# l1=[]
# for num in l:
#     l1.append(num**2)
# print(l1)

# def square(l):
#     l1 = []
#     for num in l:
#         l1.append(num ** 2)
#     return(l1)
# print(square([2,3,4,5,6,9,7]))


#wapt to search a specified character in given call is return its position
# ('hello','l')
def position(s,char):
    for i,v in enumerate(s):
        if v==char:
            return i

print(position('hello','l')) #2

##WAPT return last digit of an integer

# a=3456789
##Chat GPT
# def get_last_digit(number):
#     return number % 10
#
# a = 3456789
# last_digit = get_last_digit(a)
# print("The last digit is:", last_digit)

# def last_digit(number):
#     return number%10
# print(last_digit(3456789))
##__________________________________________________________
# a= 3456789
def last_digit(num):
    return num%10

print(last_digit(23456))   #6

#WAPT return a list if words is even length reversed it else keep as it is
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
##Using for loop##
name1=[]
#for name in names:
#    if len(name) %2==0:
#        name1.append(name[::-1])
#    else:
#        name1.append(name)
#using function
def even_rev(names):
    return [ name[::-1] if len(name) % 2==0 else name for name in names]
print(even_rev(names))

#['apple', 'yahoo', 'elgoog', 'gmail', 'walmart', 'trakpilf', 'koobecaf', 'nozama']

# WAPT  check list is homogenous or not
# [12,3.8,56,78]

def homo_hetro(lst):
    for ele in lst:
        if type(ele)!=type(lst[0]):
            print('heterogeneous')
            break
    else:
        print('homogenous')
homo_hetro([12,77,56,78])  #homogenous


#WAPT reverse a string or list or tuple
# #From Chat GPT
# def reverse_input(input_data):
#     if isinstance(input_data, str):
#         return input_data[::-1]  # Reverse a string
#     elif isinstance(input_data, list):
#         return input_data[::-1]  # Reverse a list
#     elif isinstance(input_data, tuple):
#         return input_data[::-1]  # Reverse a tuple
#     else:
#         return "Unsupported type"  # For unsupported types
#
#
#
#
# string_example = "Hello, World!"
# reversed_string = reverse_input(string_example)
# print("Reversed String:", reversed_string)
#
# # Reversing a list
# list_example = [1, 2, 3, 4, 5]
# reversed_list = reverse_input(list_example)
# print("Reversed List:", reversed_list)
#
#
#
#
# '''
# tuple_example = (10, 20, 30, 40)
# reversed_tuple = reverse_input(tuple_example)
# print("Reversed Tuple:", reversed_tuple)
# '''
# #_____________________________________________________________________________
def reverse(value):
    if isinstance(value ,(list,str,tuple)):
        return value[::-1]
    else:
        return f'{type(value)} has no attribute called reverse'
print(reverse('python'))
print(reverse([2,3,4,4,6]))
print(reverse({'s':3,'f':9}))
#2nd Method
## def reverse(coll):
##     for ele in coll:
##         if type(ele) not in [str,list,tuple]:
##             print('Other than the listed data')
##         else:
##             print("items from the required type")
## print(reverse('python'))
## print(reverse([2,3,4,4,6]))
## print(reverse({'s':3,'f':9}))


#Write a program  to check whwether the number is even or odd
def prim(num):
    if num % 2==0:
        return 'even number'
    else:
        return 'odd number'
print(prim(11))

#Write a program  to check whwether the number is prime number
# wapt to Check the given number is Prime Number
# 1--> 1 -->p
# 2--> 2 -->p
# 3--> 3 -->p
# 4--> 2,4 --> np
# 5--> 5 --> p
# 6--> 2,3,6 -->np
# 7 -->7 -->p
# 28 --> 2,4,7,8
# 29 --> 29 -->p
def prime_number(num):
    for i in range(2,(num//2)+1):
        if num%i==0:
            print('not a prime number')
            break
    else:
        print('prime number')
prime_number(19)
