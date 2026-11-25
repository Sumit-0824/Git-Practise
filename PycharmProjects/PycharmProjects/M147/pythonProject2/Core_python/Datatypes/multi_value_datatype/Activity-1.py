###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print(s[0])
# 'o'
print(s[-1])
# 'djan'
print(s[:4])
# 'jan'
print(s[1:4:1])
# 'go'
#print(s[4:])  #or print(s[-2:])

# Bonus: Use indexing to reverse the string
print(s[::-1])       #ognajd

###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
#
l[2][2]="goodbye"
print(l)    #[3, 7, [1, 4, 'goodbye']]




###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])


###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))    #{1, 2, 3}

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:[fstring]
"Hello my dog's name is Sammy and he is 4 years old"
print(f"Hello my dog's name is {name} and he is {age} years old")



###############
## Problem 6 ##
###############
# Write a program to replace one string with another. e.g. "Hello World"
# replaces "World" with "Universe"
s =  "Hello World"
print("Hello World".replace('World','universe'))





###############
## Problem 7 ##
###############
# Write a program to swap two numbers without using the 3rd variable.
a = 10
b = 20

a,b=b,a
print(a)
print(b)



