# Comperhension:it is phenomenon of creating a new o/p collection by
# reducing the number of instrution taken to do the required operation.
#Comprehension can be done only for mutable collection-List,Set and Dictionary
# comperhension is classified into 3 type:
# list comperhension
# set comperhension
# dict comperhension

# list comperhension : it is phenomenon of creating a new list collection by
# reducing the number of instruction
#IMPORTANT
#For loop without any condition-# var_name = [expression <for loop>]
#For loop without with condition-# var_name = [expression <for loop> <if condition>]
#For loop with if and else statement-# var_name = [Texp <if condition> <else> Fexp <for loop>]
#For Nested loop- check line 83


#number in range 1-20 in a list by using for loop
l = []
for i in range(1,21):
    l.append(i)
print(l)
#1.For loop without any condition
# var_name = [expression <for loop>]
numbers = [num for num in range(1,21)]
print(numbers)

#list of square
l = [2,4,6,8,3]
square = [num**2 for num in l]
print(square)

#list of -ve number using for loop
nums = [3,4,6,8,2,9]
negative_num= [-num for num in nums]
print(negative_num)


#2.For loop with with condition
#var_name = [expression <for loop> <if condition>]
#even numbers in range 1-20
l = []
for i in range(1,21):
    if i%2==0:
        l.append(i)
print(l)

even = [num for num in range(1,21) if num%2==0]
print(even)

#list of vowels character from string
s = 'python programming'
#o/p:['o','o','a','i']
vowels = [char for char in s if char in 'aeiou']
print(vowels)

# list of palindromes
names = ['steve','eve','john','stella','anna','bob']
#o/p:['eve','anna','bob']
pali = [name for name in names if name == name[::-1]]
print(pali)

#return a list starting char is vowels in the string
names = ['laura','stevs','bill','james','bob','greig','scott','alex','ive']
#o/p: ['alex','ive']
res = [name for name in names if name[0] in 'eaiou']
print(res)


#3.For loop with if and else statement
#var_name = [Texp <if condition> <else> Fexp <for loop>]
#range 1-20   : even :append that to list  odd :str(num) and append
# ['1',2,'3',4,'5',...]
numbers = [num if num%2==0 else str(num) for num in range(1,21)]
print(numbers)
#Output-['1', 2, '3', 4, '5', 6, '7', 8, '9', 10, '11', 12, '13', 14, '15', 16, '17', 18, '19', 20]
#list of words with even length words kept as is and the odd length words reversed
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
word_rev = [name if len(name)%2==0 else name[::-1] for name in names ]
print(word_rev)

#Output---['elppa', 'oohay', 'google', 'liamg', 'tramlaw', 'flipkart', 'facebook', 'amazon']





'''
DRAW BACK:
1. assignment operators cannot be used
2. loop control statements cannot be used
3. elif statements can't be used

'''
list_ = [[1,2,3],[4,5,6],[7,8,9]]
# o/p:[1,2,3,4,5,6,7,,8,9]
print([i for ele in list_ for i in ele])
#Output--[1, 2, 3, 4, 5, 6, 7, 8, 9]
# list of index and element pair
s = 'hello'
res = [(i,v) for i,v in enumerate(s)]
print(res)
#Output--[(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
#list of number raised to the power of their corresponding indices
nums = [1,2,3,4]
# o/p:[1**0,2**1,3**2,4**3] = [1,2,9,64]
print([v**i for i,v in enumerate(nums)])
#Output-[1, 2, 9, 64]
# Building a list of first_name and last_name from full_names
full_names = ["steve jobs", "bill gates", "john doe", "tim cook"]
# extracting first_name and last_name using list comprehension


# list of words starting with "p"
sentence = " Python is a programming language"

# list of elements if the element is a string reverse it else keep it as is
items = ["hello", 12, "python", True, 12.1]

# Filtering out those names which are less than 6 characters
names = ['laura','stevs_jobs','bill_gates','james_doe','bob','greig','scott','alex','ive']
#Assignment in Comprehension_assignment
# --------------------------------------------------------------------------------------------
