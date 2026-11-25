
###FOR LOOP LIST CONCEPT##########
#Traversing through list
# fruits = ['apple', 'orange', 'banana', 'strawberry']
#
# for ele in fruits:
#     print(ele)
##output-
'''
apple
orange
banana
strawberry
'''
#Traversing and Updating in list
# fruits = ['apple', 'orange', 'banana', 'strawberry']
# l = []
# for ele in fruits:
#     l.append(ele)
# print(l)
##output-['apple', 'orange', 'banana', 'strawberry']

#WAP to get the following output
# l=[1,2,3,'hello','hii',-5,-4]
# l1=[]   #create empty list
# for ele in l:
#     if type(ele)==int:
#         l1.append(abs(ele))
# print(l1)
##output--[1, 2, 3, 5, 4]
# l=[33,45,22,86,67,94,31,56]
# even=[]
# odd =[]
# for num in l:
#     if num%2==0:
#         even.append(num)
#         #print(even)
#     else:
#         odd.append(num)
#         #print(odd)
# print(even)
# print(odd)
## o/p: even = [22,86,94,56]
## odd = [33,45,67,31]
#WAP to sum all the numbers in the given string
# sentence = 'hello 123 world 567 welcome to 9724 python'
# res=0
# for char in sentence:
#     if char.isdigit():
#         res = res + int(char)
# print(res)
##output-->46
#WAP to sum all the even numbers in the given string
# sentence = 'hello 123 world 567 welcome to 9724 python'
# res=0
# for char in sentence:
#     if char.isdigit() and int(char)%2==0:
#         res = res + int(char)
# print(res)
##output-->14
# wap to get the greatest  integer number from the homogeneous list
# num = [3,55,233,23344,66,77,1,10]
#
# greatest_num=max(num)
# for ele in num:
#     if ele==greatest_num:
#         print(f'{ele} is greatest')
##output-23344 is greatest

# Write a program to extract all the unique words which starts with letter 'h'

# Given string
string = 'hello world hi hello universe how are you happy birthday'

# Split the string into words
words = string.split()
#print(words)
##-->['hello', 'world', 'hi', 'hello', 'universe', 'how', 'are', 'you', 'happy', 'birthday']
# # Set to store unique words starting with 'h'
unique_words = set()

# Loop through each word in the list
for word in words:
    if word.lower().startswith('h'):  # Check if the word starts with 'h' (case insensitive)
        unique_words.add(word.lower())  # Add the word to the set to ensure uniqueness

# Print the unique words starting with 'h'
print("Unique words starting with 'h':", unique_words)
#Output--Unique words starting with 'h': {'happy', 'how', 'hello', 'hi'}


