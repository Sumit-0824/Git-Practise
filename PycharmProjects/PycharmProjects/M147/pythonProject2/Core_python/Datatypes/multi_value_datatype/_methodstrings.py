
#print(msg.index('a'))---It throw error
#print(msg.find('a'))-- it gives -index.it does not throw error

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
print(s[-4])  #o
print(s[1])   #e
print(s[-2])  #l
print(s[2])   #l
# print(s[11]) #error
# print(s[2,5]) #error

# --------------------------------------------------------------------------------
# slicing:A process of extracting multiple character at a time.
# syntax: var_name[startindex:endindex(+/-1):stepvalue]
#                     0        len of coll      1
print(s[-4:2-1:-1])           #ow oll
msg = 'Good Morning'
print(s[::])                  #hello world
print(s[::-1])                #dlrow olleh
print(msg[0:3+1:1])           #Good
print(msg[3::-1])             #dooG
# Morning
print(msg[5:12:1])            #Morning
print(msg[5::1])              #Morning
# od Morn
print(msg[2:-4+1:1])
print(msg[2:-3:1])
# nroM do
print(msg[-4:1:-1])
print(msg[-4:2-1:-1])
#
print(msg[::])               #Good Morning
print(msg[::2])              #Go onn
print(msg[::3])              #Gdoi
print(msg[::-1])             #gninroM dooG
print(msg[::-2])             #girMdo
print(msg[::-3])             #gnMo

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
print(msg.capitalize())                    # o/p----Welcome to python
print(msg)                                 #o/p---- welcomE To PythoN
# upper()
print(msg.upper())                         #o/p-----WELCOME TO PYTHON
# lower()
print(msg.lower())                         #o/p-----welcome to python
# swapcase
print(msg.swapcase())                      #o/p-----WELCOMe tO pYTHOn
# count
print(msg.count('o'))                      #o/p-----3
print(msg.count('o',0,15)) #o/p-----2
# index
msg = 'welcomE To PythoN'
print(msg.index('P'))                      #o/p-----11
print(msg.index('o'))                      #o/p-----4    #first occurance
print(msg.rindex('o'))                     #o/p-----15   #last occurance
# print(msg.index('a'))                    #o/p-----will throw error

# find
print(msg.find('P'))                       #o/p-----11
print(msg.find('o'))                       #o/p-----4
print(msg.rfind('o'))                      #o/p-----15
print(msg.find('a'))                       #o/p------1 will execute and give the negative index
print("today is beautiful day".find("day"))#o/p------2
print("today is beautiful day".rfind("day"))#o/p-----19
# startswith()
print(msg.startswith('w'))                 #o/p------True
print(msg.startswith('p'))                 #o/p------False

# endswith()
print(msg.endswith('N'))                   #o/p------True
print(msg.endswith('t'))                   #o/p------False

# 'replace'
print(msg.replace('o','a'))    #o/p------welcamE Ta PythaN
print('hello world'.replace('world','universe'))  #o/p-----hello universe

msg = 'welcomE To PythoN class'

# split()
print(msg.split())                          #o/p-----['welcomE', 'To', 'PythoN', 'class']
print(msg.split('o',2))        #o/p-----['welc', 'mE T', ' PythoN class']
print(msg.rsplit('o',2))       #o/p-----['welcomE T', ' Pyth', 'N class']

# strip
s = '               hello world                '
print(s.strip())                            #o/p-----hello world
print(s.lstrip())                           #o/p-----hello world
print(s.rstrip())                           #o/p-----               hello world

# join
print(' '.join(['welcomE', 'To', 'PythoN', 'class'])) #o/p----welcomE To PythoN class
# print('@'.join('hello'))

#
print('asd123'.isalnum())                   #o/p--------- True
print('asd123'.isdigit())                   #o/p--------- False
print('asd123'.isalpha())                   #o/p--------- False
print('asd'.isalpha())                      #o/p--------- True
print('asd'.islower())                      #o/p--------- True
print('asd'.isupper())                      #o/p---------  False
print('ASDF'.isupper())                     #o/p--------- True
print(' '.isspace())                        #o/p--------- True
# -----------------------------------------------------------------------------
# concatenation
a = 'hai'
b= 'hello'
c = 'good'
d = 'evening'
print(a+' '+b+' '+c+' '+d)                 #hai hello good evening

# replication
# str*int
# ---------------------------------------------------------------------------------
string = "Hi Welcome to python"
# # 1. Print Even index Characters of string.
print(string[::2])   #H ecm opto
# # 2. Print Every Alternate Characters in reverse order
print(string[::-2])  #
# # 3. Print the string in reversed order
print(string[::-1]) #nohtyp ot emocleW iH
# # 4. Print extension of the filename
a = 'Youtube.txt'
print(a[8:])       #txt
#
# # 5. Print only filename
print(a[:7])       #Youtube
# # 6. Printing only protocol in
url = 'https://google.com'
print(url[:5])     #https
# ----------------------------------------------------------------------------------
# 1.Convert the string into comma separated string.
a = "hai welcome to Python"
print(a.split())
# 2. Difference between find( ) and index( )
#find() returns -1 as output if it is unable to find the substring, whereas index() returns a ValueError exception
# 3. How to check whether a string is empty?
s = ''
print(len(s))
# 4. Check if the string contains only numbers.
print(a.isdigit())
# 5. Reverse the above string
rev_str=a[::-1]
print(rev_str)












