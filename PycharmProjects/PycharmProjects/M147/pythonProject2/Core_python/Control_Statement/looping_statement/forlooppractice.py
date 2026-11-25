#1.Write a program to print numbers from 1 to 10 using a for loop
# for i in range(11):
#     print(i,end=' ')
#Output-0 1 2 3 4 5 6 7 8 9 10
#2.Given a list of integers, use a for loop to calculate the sum of all the elements in the list.
# numbers = [1, 2, 3, 4, 5]
# sum=0
# for i in numbers:
#     sum=sum+i
# print(sum)
##Output--15
#3. Find the Maximum Number in a List
# numbers = [10, 20, 4, 45, 99]
# max_num=max(numbers)
# for i in numbers:
#      if i==max_num:
#          print(f'{i} is greatest')
#Output-99 is greatest
#4. Print Even Numbers from 1 to 20
# for i in range(21):
#     if i%2==0:
#         print(i,end=' ')
#output--0 2 4 6 8 10 12 14 16 18 20
#5. Count the Number of Vowels in a String
#string = "hello world"
# s=''
# for char in string:
#     if char in 'aeiou':
#         s=s+char
# print(s)
# print(len(s))
#output-eoo
#output-3

#6. Reverse a String Using a for Loop
# string = "Python"
# s=''
# for char in string:
#     s=char+s
# print(s)
#Output-nohtyP
#7. Print a List of Numbers Squared
#Given a list of integers, use a for loop to print the square of each number.
numbers = [2, 4, 6, 8]
new_num=[]
for num in numbers:
    new_num= num**2
    print(new_num)
#output-- 4 16 36 64



# 8. Find the Factorial of a Number
# Write a program that calculates the factorial of a number using a for loop.
# num = 5  # The factorial of 5 is 5 * 4 * 3 * 2 * 1
# factorial = 1
#
# # Use a for loop to calculate the factorial
# for i in range(1, num + 1):
#     factorial *= i  # Multiply factorial by each number from 1 to num
#
# print(f"The factorial of {num} is {factorial}")

# output--->120

# 9. Create a List of Odd Numbers from 1 to 50
# Use a for loop to generate a list of odd numbers between 1 and 50.
# l=[]
#
# for i in range(50):
#     if i%2!=0:
#         l.append(i)
# print(l, end='')

# Output--[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

# 10. Check if a Word is a Palindrome
# Use a for loop to check if a given string is a palindrome (reads the same forwards and backwards).
word = "madam"

if word==word[::-1]:
    print('palindrome')
else:
    print('not palindrome')


##Out put--Palindrome
#11. Print a Multiplication Table
#Write a program that uses a for loop to print the multiplication table for a given number.
#multiplication of 5
# num=int(input('Enter the number: '))
# for i in range(1,11):
#     print(f'{num}*{i}={num*i}')
##output
'''
5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
5*6=30
5*7=35
5*8=40
5*9=45
5*10=50

'''


#Create a Dictionary from Two Lists
# Given two lists, one of keys and one of values, use a for loop to create a dictionary by pairing each key with its corresponding value.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d={}
for v1,v2 in zip(keys,values):
    d[v1]=v2
print(d)
##output-{'a': 1, 'b': 2, 'c': 3}
