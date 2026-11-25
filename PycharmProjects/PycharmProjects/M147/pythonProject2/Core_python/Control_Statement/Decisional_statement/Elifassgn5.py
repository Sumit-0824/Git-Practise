 #WAP to check the char is upper case or lower case or digit or special symbol by taking
# user input without using inbuilt methods.

# Char=input('Enter the Char:')
# if Char >='A' and Char <='Z':
#     print(f'{Char}is uppercase')
# elif Char >='a' and Char <='z':
#     print(f'{Char} is lowercase')
# elif Char >='0' and Char<='9':
#     print(f'{Char} is digit')
# else:
#     print(f'{Char} is Special Symbol')




# WAP to check given string is starting with upper case or lower case or digit
# or special symbol. if it is upper print "startswith upper case", if it is lower
# print "startswith lower case" and same as for digit and special symbols.

s= input('Enter the String:')
if s[0].isupper():
    print(f'{s} startswith upper case')
elif s[0].islower():
    print(f'{s} startswith lower case')
elif s[0].isdigit():
    print(f'{s} startswith digit')
else:
    print(f'{s} startswith Special Symbols')
