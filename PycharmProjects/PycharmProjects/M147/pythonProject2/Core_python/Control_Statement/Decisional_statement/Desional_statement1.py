# CONTROL STATEMENTS: the statement which will control flow of execution
# 2type:
# 1. decision/conditional statements
# 2. looping statements

# 1. decision/conditional statements : Conditional statement are those statement
# which will decide what to be done if the condition is True and what to be
# done if condition is False
#We will use simple if when we are having 1 condition and 1 statement
#If statement is True it will print the statement else it will not go inside the statement
# 4 types:
# simple if
# if else
# elif
# nested if

# simple if : one condition and only one statement
# syntax:
# if <condition>:
#     TSB

# Write a program to check the given number is positive.
# num = int(input('enter the number:'))
# if num>0:
#     print(f'{num} is +ve number')

# Write a program to check given number is even.
# num = int(input('enter the number:'))
# if num%2==0:
#     print(f'{num} is even')

# WAPT check given number is division by 5 and 3.
# num = int(input('enter the number:'))
# if num%5==0 and num%3==0:
#     print(f'{num} is divisble by 5 and 3')

# WAPT check the string starting with vowel.
# s = 'anna'
# # if s[0] == 'a' or s[0]=='e' or s[0]=='i' or s[0]=='o'or s[0]=='u':
# if s[0] in 'aeiou':
#     print('string starting with vowel')

# WAPT check whether the character is uppercase.
letter= input('enter the letter: ')
# if letter.isupper():
#    print(f'{letter} is uppercase')
if letter>='A'and letter<='Z':
    print(f'{letter} is uppercase')


# WAPT check whether given character special symbol .
# c= input('enter the symbol: ')
# if not c.isalnum():+
#    print(f'{c} is special symbol')


# WAPT check whether the given data is single value data or not
# d=eval(input('Enter the data: '))
# if type(d)== int or type(d)== float or type(d)==complex or type(d) ==bool:
#    print(f'The {d} is single value')



# WAPT check whether the given string is having more than 5 characters .
# st = input("Enter string: ")
# stc = len(st)
# if stc > 5:
#     print("Entered string have more than 5 characters. ")






