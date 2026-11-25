# type of arguments:
# 1. positional args
# 2. keyword args
# 3. combination of the positional args keyword args
# 4. only positional args
# 5. only keyword args
# 6. combination of positional args and keyword args
# 7. variable positional args
# 8. variable keyword args


def display(name,age):
    print(f'my name is {name} and i am {age} years old')

display('anna',45)   #positional args---------------------1
display(name = 'steve',age = 23)   # keyword args--------------------2
display('bill' ,age = 43)   # combination----------------------3
# display(name = 'anna',67)   # error  ...Keyword args should be written after positional arguments

#4. only positional agrs:  here before the (/)slash it can be having any number
# of parameter all the parameter should be positional args

def add(a,b,/,c,d):
    print(a+b+c+d)
add(2,3,4,5)
# add(a = 2,b = 5,c= 5,d = 7)
add(4,6,c = 3,d = 8)

#5. only keyword args: here after the asterisk(*) it can have any number of paramenter
# it accept only keyword args
def add(a,b,*,c,d):
    print(a+b+c+d)

# add(2,3,4,5)
add(a = 7,b = 8,c= 7,d = 5)
add(3,5,c = 9,d = 7)

# 6. combination of positional args and keyword args
def add(a,b,/,*,c,d):
    print(a+b+c+d)
add(2,6,c = 9,d= 6)   #23

# 7. variable positional args:(*args)
def add(*args,a,b):
    print(args)
    print(sum(args))

add(4,5,6,2,5,6,7,8,a = 6,b = 8)
#43
# 8.variable keyword args:(**kwargs): We can pass any no. of keyword argument
def display(**kwargs):
    print(kwargs)

display(a = 2,b= 3,c = 4)

#output-{'a': 2, 'b': 3, 'c': 4}
# default values:

def greet(name = 'world'):
    print(f'hello {name}')

greet('anna')     #hello anna
greet()           #hello world





# # ------------------------------------------------------------------------------
# # 1.strong number     #A number is called strong number if sum of the factorial of its digit is equal to number itself
# #Example= 145= 1!+4!+5!
# import math
# def strong_number(num):
#     digits = str(num)             ## Convert the number to a string to iterate over its digits
#     sum_of_factorials = 0         ## Calculate the sum of factorials of the digits
#     for digit in digits:
#         sum_of_factorials += math.factorial(int(digit))
#     return sum_of_factorials == num   # Check if the sum of factorials is equal to the original number
# print(strong_number(145))
#
# # # Example usage
# # number = int(input("Enter a number to check if it's a strong number: "))
# #
# # if strong_number(number):
# #     print(f"{number} is a strong number.")
# # else:
# #     print(f"{number} is not a strong number.")
#
#
# #2. perfect number
# # #In number theory, a perfect number is a positive integer that is equal to the sum of its posit
# # ive proper divisors
# #Example-6- 1+2+3, 28-1+2+4+7+14
# def perfect_number(num):
#     divisors_sum = 0
#
#     for i in range(1, num):
#         if num % i == 0:
#             divisors_sum += i
#     return divisors_sum == num
#
# print(perfect_number(8))
# # # Example usage
# # number = int(input("Enter a number to check if it's a perfect number: "))
# #
# # if perfect_number(number):
# #     print(f"{number} is a perfect number.")
# # else:
# #     print(f"{number} is not a perfect number.")
#
#
# #3. neon number--A neon number is a number where the sum of digits of square of the number is equal to the number.
# # For example if the input number is 9, its square is 9*9 = 81 and sum of the digits is 9
# def neon_num(n):
#     square = n ** 2
#     sum_of_digits = 0
#     for digit in str(square):
#         sum_of_digits += int(digit)
#     if sum_of_digits == n:
#         return True
#     else:
#         return False
#
# print(neon_num(12))
# # # Example usage:
# # number = int(input("Enter a number: "))
# # if neon_num(number):
# #     print(f"{number} is a Neon number.")
# # else:
# #     print(f"{number} is not a Neon number.")
#
# # spy number
# #A spy number is a number where the sum of its digits is equal to the product of its digits. For example, 112 is a spy number because:
#
# #Sum of digits: 1 + 1 + 2 = 4
# #Product of digits: 1 * 1 * 2 = 4
#
# def spy_number(num):
#     digits = str(num)       # Convert the number to a string to iterate over its digits
#
#     # Initialize sum and product
#     sum_of_digits = 0
#     product_of_digits = 1
#
#     # Calculate sum and product of digits
#     for digit in digits:
#         sum_of_digits += int(digit)
#         product_of_digits *= int(digit)
#
#     # Check if sum and product are equal
#     return sum_of_digits == product_of_digits
#
# print(spy_number(4))
# # # Example usage
# # number = int(input("Enter a number to check if it's a spy number: "))
# #
# # if spy_number(number):
# #     print(f"{number} is a spy number.")
# # else:
# #     print(f"{number} is not a spy number.")
#
# # happy number
# '''
# A happy number is a number that eventually reaches 1 when you repeatedly replace the number by the sum of the squares of its digits. If a number is not happy, it will end up in a cycle that doesn't include 1.
#
# For example:
#
# 19 is a happy number:
# 1² + 9² = 1 + 81 = 82
# 8² + 2² = 64 + 4 = 68
# 6² + 8² = 36 + 64 = 100
# 1² + 0² + 0² = 1 + 0 + 0 = 1 (so, 19 is a happy number).
# '''
# # armstrong number
# '''
# An Armstrong number (also known as a Narcissistic number or Pluperfect number) is a number that is equal to the sum of its own digits raised to the power of the number of digits.
#
# For example:
#
# 153 is an Armstrong number because:
# 1³ + 5³ + 3³ = 1 + 125 + 27 = 153.
# '''
#
#
# def armstrong_number(num):
#     # Convert the number to a string to easily iterate over its digits
#     digits = str(num)
#     n = len(digits)  # Number of digits
#
#     # Calculate the sum of digits raised to the power of n
#     sum_of_powers = sum(int(digit) ** n for digit in digits)
#
#     # If the sum is equal to the original number, it is an Armstrong number
#     return sum_of_powers == num
#
# print(armstrong_number())
#
# # # Example usage
# # number = int(input("Enter a number to check if it's an Armstrong number: "))
# #
# # if armstrong_number(number):
# #     print(f"{number} is an Armstrong number.")
# # else:
# #     print(f"{number} is not an Armstrong number.")
#
# # sunny number
# '''
# A sunny number is a number that is one less than a perfect square. In other words, if you add 1 to the number, the result should be a perfect square.
#
# For example:
#
# 8 is a sunny number because 8 + 1 = 9, which is a perfect square (3² = 9).
# '''
#
# import math
#
# def sunny_number(num):
#     # Check if num + 1 is a perfect square
#     return math.isqrt(num + 1) ** 2 == num + 1
#
# # Example usage
# number = int(input("Enter a number to check if it's a sunny number: "))
#
# if sunny_number(number):
#     print(f"{number} is a sunny number.")
# else:
#     print(f"{number} is not a sunny number.")
#
# print(sunny_number(8))