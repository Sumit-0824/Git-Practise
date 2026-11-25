#1.
# 1. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
#     except the first char itself.
# 	s = 'restart'
# 	o/p : 'resta$t'
# s = 'restart'
# first_char = s[0]
# modified_string = first_char + s[1:].replace(first_char, '$')
# print(f"Modified string: {modified_string}")

#6. Check if a specific value (7) exists in a set
# s ={1,2,3}
#
# s ={1,2,3}
# value = 7
#
# if value in s:
#     print(f'{value} exists in the set.')
# else:
#     print(f'{value} does not exist in the set.')


#18.Take input of age of 3 people by user and determine oldest and youngest among them
# age1 = int(input("Enter age of User 1: "))
# age2 = int(input("Enter age of User 2: "))
# age3 = int(input("Enter age of User 3: "))
#
# oldest = max(age1, age2, age3)
# youngest = min(age1, age2, age3)
#
# print(f"The oldest User is {oldest} years old.")
# print(f"The youngest User is {youngest} years old.")


#19.Take values of length and breadth of a rectangle from user and check if it is square or not.

# length = float(input("Enter the length of the rectangle: "))
# breadth = float(input("Enter the breadth of the rectangle: "))
#
# if length == breadth:
#     print("The shape is a square.")
# else:
#     print("The shape is a rectangle.")

#20. Write a program to print absolute value of a number entered by user.
'''
 E.g.-
	INPUT: 1        OUTPUT: 1
	INPUT: -1        OUTPUT: 1
'''

# number = int(input("Enter a number: "))
#
# absolute_value = abs(number)
# print(f"The absolute value of the number is: {absolute_value}")


#21. Write a program to check if a year is leap year or not.
#NOTE: If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0): #or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# 22. A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one.
# E.g.-
# 	INPUT : 1234        OUTPUT : 4321
# 	INPUT : 5982        OUTPUT : 2895


# number = input("Enter a 4-digit number: ")
#
#
# if len(number) == 4 and number.isdigit():
#
#     reversed_number = number[::-1]
#     print(f"The reversed number is: {reversed_number}")
# else:
#     print("Please enter a valid 4-digit number.")
