# string :
# A String is a sequence of characters enclosed within single quotes or double quotes or three
# single quotes/three double quotes.
# syntax:
# var_name = 'collection of char'
# var_name = "collection of char"
# var_name = '''collection of char''' or """coll of char"""


msg = 'Happy new year!:-) Welcome to the 2025'
msg1 = "Happy new year!:-) Welcome to the 2025"
msg2 = '''Happy new year!:-) Welcome to the 2025'''

greet = "welcome to python's class"
message = '''this multiline string
hello all welcome to python programing lang
this is new line
'''
print(message)
print(len(msg))
# ------------------------------------------------------------------------------
# raw string : prefixed with "r" or'R'
# # Raw string will treat backslashes as a part of a string.

s = r'hello \task from pytho\n world'
print(s)

f = R'C:Users\QSP\Desktop\traning\OneNote_RecycleBin'
print(f)
# -------------------------------------------------------------------------------------
# indexing:- A process of extracting single character at a time.
# - Indexing can be positive(starts with 0)or negative(starts with -1)

# var_name[index]
s = 'hello world'
print(s[-4])
print(s[1])
print(s[-2])
print(s[2])
# print(s[11]) #error
# print(s[2,5]) #error

# --------------------------------------------------------------------------------
# slicing:A process of extracting multiple character at a time.
# syntax: var_name[startindex:endindex(+/-1):stepvalue]
#                     0        len of coll      1
print(s[-4:2-1:-1])
msg = 'Good Morning'
print(s[::])
print(s[::-1])
print(msg[0:3+1:1])
print(msg[3::-1])
# Morning
print(msg[5:12:1])
print(msg[5::1])
# od Morn
print(msg[2:-4+1:1])
print(msg[2:-3:1])
# nroM do
print(msg[-4:1:-1])
print(msg[-4:2-1:-1])
#
print(msg[::])
print(msg[::2])
print(msg[::3])
print(msg[::-1])
print(msg[::-2])
print(msg[::-3])

# String formatting:Infusing data dynamically into a string during the time of
# execution or runtime is called formatting.
# • There are 3 ways of string formatting
#     Formatting with placeholders.
#     Formatting with .format() string method
#     Formatting with string literals called f-string


#  Formatting with string literals called f-string: prefixed with "f"
# {} --> placeholder

first_name = 'anna'

print(f'welcome {first_name}')

a = 24
b = 'day'
print(f'there are {a} hours in {b}')
print(f'one {b} has {a*60} min')

# -----------------------------------------------------------------------------------------
# method in string
print(dir(str))
# print(dir('hello'))
# print(dir(msg))
msg = 'welcomE To PythoN'
# var_name.method_name
# 'capitalize'
print(msg.capitalize())
print(msg)
# upper()
print(msg.upper())
# lower()
print(msg.lower())
# swapcase
print(msg.swapcase())
# count
print(msg.count('o'))
print(msg.count('o',0,15))
# index
print(msg.index('P'))
print(msg.index('o'))
print(msg.rindex('o'))
# print(msg.index('a'))

# find
print(msg.find('P'))
print(msg.find('o'))
print(msg.rfind('o'))
print(msg.find('a'))

# startswith()
print(msg.startswith('w'))
print(msg.startswith('p'))

# endswith()
print(msg.endswith('N'))
print(msg.endswith('t'))

# 'replace'
print(msg.replace('o','a'))
print('hello world'.replace('world','universe'))

msg = 'welcomE To PythoN class'

# split()
print(msg.split())
print(msg.split('o',2))
print(msg.rsplit('o',2))

# strip
s = '               hello world                '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# join
print(' '.join(['welcomE', 'To', 'PythoN', 'class']))
# print('@'.join('hello'))

#
print('asd123'.isalnum())
print('asd123'.isdigit())
print('asd123'.isalpha())
print('asd'.isalpha())
print('asd'.islower())
print('asd'.isupper())
print('ASDF'.isupper())
print(' '.isspace())
# -----------------------------------------------------------------------------
# concatenation
a = 'hai'
b= 'hello'
c = 'good'
d = 'evening'
print(a+' '+b+' '+c+' '+d)

# replication
# str*int
# ---------------------------------------------------------------------------------
# string = "Hi Welcome to python"
# # 1. Print Even index Characters of string.
#
# # 2. Print Every Alternate Characters in reverse order
#
# # 3. Print the string in reversed order
#
# # 4. Print extension of the filename
# a = 'Youtube.txt'
#
#
# # 5. Print only filename
#
# # 6. Printing only protocol in
# url = 'https://google.com'
# ----------------------------------------------------------------------------------
# 1.Convert the string into comma separated string.
a = "hai welcome to Python"

# 2. Difference between find( ) and index( )
#
# 3. How to check whether a string is empty?
s = ''

# 4. Check if the string contains only numbers.

# 5. Reverse the above string
rev_str=











