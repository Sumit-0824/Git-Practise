# if else:
# 1 condition and 2 statements
# syntax:
'''
if <condition>:
    TSB
else:
    FSB

'''

#1.WAPT check whether the character is lowercase
# letter= input('enter the letter: ')
# if letter.islower():
#     print(f'{letter} is lowercase')
# else:
#     print(f'{letter} not lowercase')

#2nd
# letter=input('enter the letter:')
# if letter>='A' and letter>='Z':
#     print(f'{letter}is uppercase')


## 2.WAPT check whether the given data is collection value data or not
# d = eval(input('Enter the data: '))
# if type(d) in[str,list,set,dict,tuple]:
#     print(f'The {d} is multi value')
# else:
#     print(f'The {d} is not  multi value')

#3.WAPT to remove duplicate if given value is collection,else print reversed value
data=eval(input('enter the value: '))
if type(data) in (str,list,tuple,set,dict):
    print(set(data))
else:
    print(str(data)[::-1])


#4.Write a program to check given number is even or not
# num = int(input('enter the number:'))
# if num%2==0:
#     print(f'{num} is even')
# else:
#     print(f'{num} is not even')

#5.Write a program to check the given character is present inside the given string or not
# String= (input('Please enter the string: '))
# char= input('Please enter the character: ')
# if char in String:
#     print('given character is present inside the given string')
# else:
#     print('not present')


