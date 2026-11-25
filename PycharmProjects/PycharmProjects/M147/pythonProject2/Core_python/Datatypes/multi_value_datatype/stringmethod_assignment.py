# 1.Convert the string into comma separated string.
a = "hai welcome to Python"
print(a.split())                   #o/p-----------['hai', 'welcome', 'to', 'Python']

# 2. Difference between find( ) and index( )
#-->find() returns -1 as output if it is unable to find the substring, whereas index() returns a ValueError exception

# 3. How to check whether a string is empty?
s = ''
print(len(s))                  #o/p------False

# 4. Check if the string contains only numbers.
print('a'.isdigit())                #o/p--------False
# 5. Reverse the above string
a = "hai welcome to Python"
rev_str= a[::-1]
print(rev_str)                           #nohtyP ot emoclew iah