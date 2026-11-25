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
#'''
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
