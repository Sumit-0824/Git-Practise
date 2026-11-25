# range:used to create the sequence of numbers b/w the specified limits.

# syntax: range(starpoint,endpoint(+/-1),updation)
#                   0                       1
# Range is not having a proper structure to display the values, so inorder to see the
# value we make use of typecasting or for loop.

# print(range(11))
# print(list(range(11)))
# print(tuple(range(1,11,2)))
# print(list(range(9,0,-1)))
#print(set(range(23,78,3)))
#print(str(range(0,10,1)))--->error
# print(dict(range(0,11)))--->error

# ---------------------------------------------------------------------------------
# for loop:is a looping statement , which is used to execute same set of instructions
# # repeatedly again and again.
# In for loop initialization and updation of looping variable in automated.

# syntax:
'''
for newvar in coll:
     statement block
'''
# coll --> range,list,str,set,tuple,dict,...


# 1.WAPT PRINT 'PYTHON' FOR 5 TIMES.

# for i in range(5):
#     print('python')
# output---->
# python
# python
# python
# python
# python

# 2.print the number in the range of 0-10
# for num  in range(0,11):
#     print(num,end = ' ')
## 0 1 2 3 4 5 6 7 8 9 10


####FOR LOOP STRING QUESTIONS#####


#msg = 'Good Morning'
# for i in range(len(msg)):
#     print(msg[i],end = '')
##output-->Good Morning
#2nd method
# s = ''
# for char in msg:
#     s = s+char #Traverse in forward direction
# print(s)
##output-->Good Morning
#4.WAP to reverse the string
# s1 = ''
# for char in msg:
#     s1= char+s1   # Reverse the string
# print(s1)
#output-->gninroM dooG
# # 5.wap to extract all the lowercase character from the given string  using for loop
#s = 'Welcome To PyThon'
# s1 = ''
# for char in s:
#     if char.islower():
#         s1 = s1+char   #Traverse in forward direction
# print(s1)
##output-->elcomeoyhon
#6.WAP to traverse in reverse direction to extract all the lowercase character from the given string  using for loop
# s = 'Welcome To PyThon'
# s1 = ''
# for char in s:
#     if char.islower():
#         s1 = char+s1   #Traverse in reverse direction
# print(s1)
##output-->nohyoemocle

#7. wap to replace all the space in the given string with underscore using for loop
# string = 'hello good evening'
#output: 'hello_good_evening'
# s = ''
# for char in string:
#     if char.isspace():
#         s = s+'_'
#     else:
#         s = s+char
#
# print(s)
##output-->hello_good_evening
##2nd method--
##print(string.replace(space,'_'))--->Go through the replace command usecase
#8.WAP to remove all the vowels from the string
#string = 'hello good morning'

# string1=''
# for char in string:
#     if char not in 'aeiouAEIOU':
#         string1=string1+char
# print(string1)
#output--->hll gd mrnng

#Write a program to print multiplication table of a given number using for loop

# num=int(input('Enter the number: '))
# for i in range(1,11):
#     print(f'{num}*{i}={num*i}')
##output
'''
Enter the number: 3
3*1=3
3*2=6
3*3=9
3*4=12
3*5=15
3*6=18
3*7=21
3*8=24
3*9=27
3*10=30

'''
#Write a program to find whether a given number is prime or not.
# num=int(input('Enter the number: '))
# for i in range(2,num):
#     if num%i==0:
#         print(f'{num} is prime')
#     else:
#         print(f'{num} is not prime')


