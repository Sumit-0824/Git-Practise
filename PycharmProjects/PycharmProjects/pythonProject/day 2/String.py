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
print(s[::])                 #hello world
print(s[::-1])               #dlrow olleh
print(msg[0:3+1:1])          #Good
print(msg[3::-1])             #dooG
# Morning
print(msg[5:12:1])            #Morning
print(msg[5::1])              #Morning
# od Morn
print(msg[2:-4+1:1])          #od Morn
print(msg[2:-3:1])            #od Morn
# nroM do
print(msg[-4:1:-1])           #nroM do
print(msg[-4:2-1:-1])         #nroM do
#
print(msg[::])                #Good Morning
print(msg[::2])               #Go onn
print(msg[::3])               #Gdoi
print(msg[::-1])              #gninroM dooG
print(msg[::-2])              #girMdG
print(msg[::-3])              #gnMo


print(dir(str))

#"Good Morning"
#'''Good Morning'''
#''Good Morning''
