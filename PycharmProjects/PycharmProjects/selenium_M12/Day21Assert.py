"""
assert keyword
syntax
assert condition,message
"""
#Ex1
a=2
b=6
'''
if a+b==6:
    print("It is correct")
else:
    raise ValueError
'''

assert a+b==8,"a and b not equal to 4"
print("It is correct")


#Ex WAPT check whether the character is lowercase
l=input("Enter the character: ")
assert l.islower(),"l is not lower"
print("It is lower")
#
