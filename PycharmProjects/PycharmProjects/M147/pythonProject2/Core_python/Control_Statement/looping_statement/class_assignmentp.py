# 1. Write a program to get all the duplicate items and the number of times the item is repeated in the list
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail", "gmail', 'gmail', 'gmail']
#
# d={}
#
# for name in names:
#      d[name] =names.count(name)
# print(d)
##output--{'apple': 3, 'google': 1, 'yahoo': 2, 'facebook': 1, 'gmail", "gmail': 1, 'gmail': 2}

#['apple', 'google', 'yahoo', 'facebook', 'gmail']

# 2. Write a program to count the number of white spaces in a given string
# s = "This is a Programming language and Programming is fun"
# count=0
# for char in s:
#     if char.isspace():
#         count=count+1
# print(count)

#Output-8


# 3. Write a program to print all the consonants in a given string
s = 'helloworld'
s1=''
for i in s:
    if i not in 'aeiou':
        s1=s1+i
        
print(s1)
##output-hllwrld


# 4. Write a program to count no of capital letters in a string
# sentence = "Hi How are You Welcome to Python"
# count=0
# for char in sentence:
#     if char.isupper():
#         count=count+1
# print(count)

#Output-5



# 5.  What is the difference between append() and extend() method in list
#Append will add 1 element in 1 time at the end ,extend will add collection in the list
#Append will add as nested list if added for than 1 item,whereas extend will add in the same linear list
# 6. Grouping Flowers and Animals in the below lists
Items = ['lotus-flower', 'lily-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
flower=[]
animal=[]
for ele in Items:
    if 'flower' in ele:
        flower.append(ele)
    elif 'animal' in ele:
        animal.append(ele)
print(flower)
print(animal)
##Output
#['lotus-flower', 'lily-flower', 'sunflower-flower']
#['cat-animal', 'dog-animal']


# 7. Replace whitespaces with newline character in the below string
# sentence = "Hello world welcome to python"
# new_sentence=sentence.replace( ' ','\n')
# print(new_sentence)
##output
'''
Hello
world
welcome
to
python
'''
# 8. Write a program to list all the number which are ending with 5 .
# numbers = ['51', '12', '123', '12345', '125', '905', '55', '15', '95655', '55555']
# num1=[]
#
# for ele in numbers:
#     if int(ele) %5==0:
#         num1.append(ele)
# print(num1)
##output-->['12345', '125', '905', '55', '15', '95655', '55555']


# 9.  Write a program to get the indexes of each item in the below lists
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
#  output should be 'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]

names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']

# Create an empty dictionary to store the indexes of each item
indexes = {}

# Iterate through the list and store the indices
for i, name in enumerate(names):
    if name not in indexes:
        indexes[name] = []
    indexes[name].append(i)

# Print the dictionary with the result
print(indexes)




# 10. Get the list of Country and City in a tuple
countries = {
    "India": ["Bangalore", "Chennai", "Delhi", "Kolkata"],
    "USA": ["Dallas", "New York", "Chicago"],
    "China": ["Beijing", "Shanghai"]
}
l=[]
for k,v in countries.items():
    for i in v:
        l.append((k,i))
print(l)
#Output--#[('India', 'Bangalore'), ('India', 'Chennai'), ('India', 'Delhi'), ('India', 'Kolkata'),  ('USA', 'Dallas'), ('USA', 'New York'), ('USA', 'Chicago'),  ('China', 'Beijing'), ('China', 'Shanghai')]

