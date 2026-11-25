# WAPT check whether the character is uppercase.
 letter= input('enter the letter: ')
 if letter.isupper():
    print(f'{letter} is uppercase')
#2nd method
#

# WAPT check whether given character special symbol .
 c= input('enter the symbol: ')
 if not c.isalnum():
    print(f'{c} is special symbol')


# WAPT check whether the given data is single value data or not
d=eval(input('Enter the data: '))
if type(d)== int or type(d)== float or type(d)==complex or type(d) ==bool:
    print(f'The {d} is single value')
#2nd method
# d = eval(input('Enter the data: '))
# if type(d) in[int,float,complex,bool]:
#      print(f'The {d} is single value')


# WAPT check whether the given string is having more than 5 characters .
 st = input("Enter string: ")
 stc = len(st)
 if stc > 5:
     print(f'Entered {st} have more than 5 characters')