# WAPT display the first 10 fibonacci number
# o/p: 0,1,1,2,3,5,8,.....
#Fibonnaci series--a sequence of numbers where each number is the sum of the two numbers before it
#1st method
# a,b=0,1
# count=0
# while count < 10:
#     print(a, end=" ")
#     a, b = b, a + b  # Update a and b to the next Fibonacci numbers
#     count += 1
##OUTPUT=0 1 1 2 3 5 8 13 21 34
#2nd method   #slighly wrong
# i1 = 0
# i2 = 1
# count = 0
# print(i1,end = ' ')
# print(i2,end = ' ')
# while count<9:
#     i = i1+i2
#     print(i,end = ' ')
#     i1 = i2
#     i2 = i
#     count +=1
##OUTPUT=0 1 1 2 3 5 8 13 21 34 55===More thsn 10 number

# WAP to print sum of the numbers by taking start and end from user.
# Start=int(input("Enter the starting number: "))
# End=int(input("Enter the Ending number: "))
#
# i=Start
# sum=0
# while i <=End:
#     sum=sum+i
#     i+=1
# print(sum)
##output
##Start=3....end=7....total=25
# # "Write a program to reverse the list as below
words = ["hi", "hello", "python"]
# o/p ['nohtyp', 'olleh', 'ih']
# l=[]
# i=0
# words=words[::-1]
# while i<len(words):
#     l.append(words[i][::-1])
#     i+=1
# print(l)
# #['nohtyp', 'olleh', 'ih']

## wap to extract a string starting with vowel character
# l = ['Apple' , 'Google' , 'amazon', 'instagram', 'gmail', 'Extract']
# l1=[]
# i=0
# while i<len(l):
#     if l[i][0] in 'aeiouAEIOU':
#         l1.append(l[i])
#     i+=1
# print(l1,end='')
# #['Apple', 'amazon', 'instagram', 'Extract']



