print("********Slicing Assisgment*******")

# ---------------------------------------------------------------------------------
string = "Hi Welcome to python"
# # 1. Print Even index Characters of string.
print(string[::2])                                        #o/p---> H ecm opto
# # 2. Print Every Alternate Characters in reverse order
print(string[::-2])                                       #o/p--->nhy teolWi
# # 3. Print the string in reversed order
rev_str= string[::-1]                                     #0/p--->nohtyp ot emocleW iH
print(rev_str)

# # 4. Print extension of the filename
a = 'Youtube.txt'                                          #o/p---->txt
print(a[8::1])     #or print(a[-3::])
# # 5. Print only filename
print(a[0:7:1])    #print(a[0:-4:1)                                        #o/p------>Youtube
# # 6. Printing only protocol in
url = 'https://google.com'
print(url[0:5:1])                                           #o/p------>https


print("**************List Class assignment *****************")
#list Slicing
# names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# # 1. Reverse the above list.
# print(names[::-1])
# #['microsoft', 'instagram', 'facebook', 'amazon', 'yahoo', 'google', 'apple']
# # 2. What is the output of names[2][3]
# print(names[2][3])
# # o
# # 3. What is the output of
# #a. names[-2: 3]
# print(names[-2: 3])
# #[]
# # 	b. names[-6:5]
# print(names[-6: 5])
# # ['google', 'yahoo', 'amazon', 'facebook']
# # 	c. names[-1:2:-1]
# print(names[-1:2:-1])
#['microsoft', 'instagram', 'facebook', 'amazon']
# 	d. names[13]
#print(names[13])
#IndexError-list out of range
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# 	e. names[:2] = ['unknown', 'Unknown']
names[:2] = ['unknown', 'Unknown']
print(names)
#['unknown', 'Unknown', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

print("******************Methods***************")


# Methods in list
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# 	1. What is the output of:
# 			a. names.append(['netflix', 'walmart', 'kroger’])
names.append(['netflix', 'walmart', 'kroger'])
print(names)
#Ans--->['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', ['netflix', 'walmart', 'kroger']]
# 			b. names.extend(['netflix', 'walmart', 'kroger'])
names.extend(['netflix', 'walmart', 'kroger'])
print(names)
#Ans---->['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', ['netflix', 'walmart', 'kroger'], 'netflix', 'walmart', 'kroger']
# 	2. What is the difference between pop, remove.
#Ans--->pop-erase the remove the element from the collection and return where as by using remove method we can remove the particular element from collection by giving particular index
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# 	3. Sort the above list in descending order.
names.sort(reverse=True)
print(names)

#Ans--->['yahoo', 'microsoft', 'instagram', 'google', 'facebook', 'apple', 'amazon']
# 	4. Sort the above list in ascending order according to their length.

names.sort(key=len)      #reverse not required
print(names)
#Ans--->['yahoo', 'apple', 'google', 'amazon', 'facebook', 'microsoft', 'instagram']
# 	5. Sort the above list in descending order according to their length.
names.sort(key=len,reverse=True)
print(names)
#---->['microsoft', 'instagram', 'facebook', 'google', 'amazon', 'yahoo', 'apple']

string = "Hi welcome to python"
# 		a. Create a list with each character of the string as its element.
# 		o/p ['h','i',' ' ,'w'.....]
#print(','.join(string))            #Ans---->H,i, ,w,e,l,c,o,m,e, ,t,o, ,p,y,t,h,o,n
print(list(string))                #['H', 'i', ' ', 'w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n']

#         b. Create a list with each word of the string as its element.
print(string.split())
#Ans--->['Hi', 'welcome', 'to', 'python']
#         o/p ['hi','welcome','to','python']





























print("**************Dictionary assignment******************")


d1 = {'a':23,'b':56,(4,5):[1,2,3],'a':56}
print(d1)         #{'a': 56, 'b': 56, (4, 5): [1, 2, 3]}--the last value will be updated as key cannot be duplicated
print(len(d1))    #3
print(d1['a'])    #56
#[1,2,3]
print(d1[(4,5)])    #Values can be accessed through keys only
print(d1['b'])      #56


d = {'a':'apple','b':[1,2,3,4,5,6],'c':{"d":'dog','p':12}}
#pple
print(d['a'][1::])

#[1,2,3,4,5,6]
print(d['b'])
#[1,3,5]
print(d['b'][::2])
#[2,4,6]
print(d['b'][1:6:2])
#[6,5,4,3,2,1]
print(d['b'][::-1])
#'og'
print(d['c']['d'][1::])
#'god'
print(d['c']['d'][::-1])
#elppa
print(d['a'][::-1])
#12
print(d['c']['p'])


# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])                    #hello
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])                      #hello
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])       #hello

print(*********Activity*********)
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



