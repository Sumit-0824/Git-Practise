# looping_statements:
# These are the control statements which are used to execute same set of
# instruction repetitively again and again .

# With the help of looping statements we can increase the efficiency of the program
# by reducing the number of instructions.

# In python looping statements got classified into 2 types:-
#  1.while loop
#  2.for loop

# 1. while loop:while is a type of looping statement which is used to execute same set of
# # instructions repetitively until the given condition becomes false.
# >>In while loop initialization of loop variable and updating of looping is must
# and should.
# >>If we do not initialize then control will through on error, if we do not update
# looping variable,it will get execute like an infinite loop.

'''
syntax:
initialization
while condition:
    statement block
    updation

'''
#1 WAPT PRINT 'PYTHON' FOR 5 TIMES.
# i = 1  # initialization
# while i<=5:  # condition
#     print('python') # statement block
#     i = i+1  # i+=1  # updation

# WAPT print number from 0-9.
# i = 0
# while i<=9:
#     print(i,end = ' ')
#     i+=1

#2.WAPT all the even number between 1-100
# i=2
# while i<=100:
#     print(i,end='')
#     i+=2

#3.WAPT to print table of given number,take input from user

# numb= int(input('Enter the number: '))   #if we will not pass it will convert to string then it will replicate
# i=1
# while i<=10:
#     print(f'{numb}*{i}={numb*i}')
#     i+=1
'''
5*1 = 5
5*2 = 10
.
.
5*10 = 50
'''
# 4.WAP to print elements of list are Even or odd.
# l = [22, 43, 56, 35, 98, 67, 52]
# i = 0
# while i<len(l):
#     if l[i]%2==0:
#         print(f'{l[i]} is even number')
#     else:
#         print(f'{l[i]} is odd number')
#     i+=1

##output
'''
22 is even number
43 is odd number
56 is even number
35 is odd number
98 is even number
67 is odd number
52 is even number
'''

#5.WAPT to find the sum of number
#n=int(input("Enter the num: "))--- user input
# n=7     #when n is given
# i=1
# res=0
# while i<=n:
#     res=res+i
#     i+=1
#     #i+=1------>It will print each iteration
# print(res)
# #output==28

'''
i = 1  n=  7    res = 0    1<7 = T   res= 0+1 = 1
i = 2           res = 1    2<7 = T   res =1+2 = 3
i = 3           res = 3    3<7 = T   res =3+3 = 6
i = 4           res = 6    4<7 = T   res =6+4 = 10
i = 5           res = 10   5<7 = T   res=10+5 = 15
i = 6           res = 15   6<7 = T   res=15+6 = 21
i = 7           res = 21   7=7 = T   res=21+7 = 28
i = 8           res = 28   8<=7= F

'''

#6.WAPT to print sum of all numbers present in list
l = [22, 54, 76, 87, 64, 42, 97, 65]

# i=0
# res=0
# while i<len(l):
#       res=res+l[i]
#       i+=1
# print(res)
#output------>507

#7.WAP to extract vowels and digits from the given string
#s = "hello world 123 hai"
#o/p---eoo123ai
# i=0
# while i<len(s):
#     if s[i] in 'aeiou' or s[i].isdigit():
#       print(s[i],end= '')
#     i+=1
#
#8.WAPT to
# a = ['hai','program','python','bye']

# d={}
# i=0
# while i<len(a):
#     d[a[i]]=len(a[i])
#     i+=1
# print(d)
# #output--{'hai': 3, 'program': 7, 'python': 6, 'bye': 3}
#9.WAPT to
# a = ['hai','program','python','bye']

# d={}
# i=0
# while i<len(a):
#     d[a[i]]=a[i][::-1]
#     i+=1
# print(d)

# #output={'hai': 'iah', 'program': 'margorp', 'python': 'nohtyp', 'bye': 'eyb'}
#10 WAPT to reverse the
s = 'Hello World 123 Hai'
i=0
while i<len(s):
    s=s[::-1]
    i+=1
print(s,end='')

##Output--->iah 321 dlroW olleH

