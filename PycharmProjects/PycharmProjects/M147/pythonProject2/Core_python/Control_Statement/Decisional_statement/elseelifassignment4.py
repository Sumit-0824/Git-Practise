#else if
# 1.WAPT check squre of given number is even or not, if it is even print 'good morning'
# # else 'good evening'
# num=eval(input('Enter the number:'))
# Sqr=num**2
# if Sqr%2==0:
#     print('Good Moring')
# else:
#     print('good evening')

#2.WAPT display if the entered age is greater than or equal to 18, print 'you are eligible to
# vote',else 'not eligible to vote'
# age=eval(input('Enter the age:'))
# if age>=18:
#     print('You are eligible to vote')
# else:
#     print('Not eligible to vote')

#elif
#3. WAP to check whether the number is negative or neutral or positive.
# WAP to check whether the number is negative or neutral or positive.
# num= eval(input("Enter the number: "))
# if num <0:
#     print(f'{num} is negative')
# elif num==0:
#     print(f'{num} is neutral')
# else:
#     print(f'{num} is positive')

## WAP to take marks of 5 sub,calculate the avg if the avg is b/w 90-100 print DISTINCTION, if 75-89 print FIRST CLASS, if it is 60-74 print SECOND CLASS, if 50-59 print THIRD CLASS, below 50 is fail. #note: max marks is 100
# m1=eval(input('Enter the marks in Subject1:'))
# m2=eval(input('Enter the marks in Subject2:'))
# m3=eval(input('Enter the marks in Subject3:'))
# m4=eval(input('Enter the marks in Subject4:'))
# m5=eval(input('Enter the marks in Subject5:'))
#
# Avg=(m1+m2+m3+m4+m5)/5       #true division since we will get in decimal
# if Avg>=90 and Avg==100:
#     print("DISTICTION")
# elif Avg>=75 and Avg<90:
#     print("FIRST CLASS")
# elif Avg>=60 and Avg<74:
#     print("Second Class")
# elif Avg>=50 and Avg<59:
#     print("Third Class")
# else:
#     print("Fail")
# WAP to check middle char of given string is vowel or not. if it is vowel print # "women are great",
# if it is consonants print "men are great" else print "God is great" # by taking user input.
# #Note: You have to pass odd length input

# s = 'flowers'
# m  = s[len(s)//2]  # s[3]
# if m in 'aeiou':
#     print("women are great")
# elif not(m.isalpha()):
#     print("God is great")
# else:
#     print("men are great")

# WAP to check the char is upper case or lower case or digit or special symbol by taking
# user input without using inbuilt methods.


Char=eval(input('Enter the Char:'))
if Char >='A' and Char >='Z':
    print(f'{Char}is uppercase')
elif Char >='a' and Char >='z':
    print(f'{Char} is lowercase')
elif Char >=0 and Char<=9:
    print(f'{Char} is digit')
else:
    print(f'{Char} is Special Symbol')


# WAP to check given string is starting with upper case or lower case or digit
# or special symbol. if it is upper print "startswith upper case", if it is lower
# print "startswith lower case" and same as for digit and special symbols.

# C=eval(input('Enter the String: '))
#
# if C[0].isupper():
#     print(f'{C} startswith upper case')
# elif C[0].islower():
#     print(f'{C} startswith lower case')
# elif C[0].isdigit():
#     print(f'{C} startswith digit')
# else:
#     print(f'{C} startswith Special Symbols')







