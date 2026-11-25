# 1.Building a list of first_name and last_name from full_names
full_names = ["steve jobs", "bill gates", "john doe", "tim cook"]
# extracting first_name and last_name using list comprehension.
#Using for loop
full_names = ["steve jobs", "bill gates", "john doe", "tim cook"]
first_names = []
last_names = []

# for name in full_names:
#     first, last = name.split()  # Split the full name into first and last name
#     first_names.append(first)
#     last_names.append(last)

print("First names:", first_names)
print("Last names:", last_names)
#Output
#First names: ['steve', 'bill', 'john', 'tim']
#Last names: ['jobs', 'gates', 'doe', 'cook']

#Using Comprehension
full_names = ["steve jobs", "bill gates", "john doe", "tim cook"]

# Extracting first_name and last_name using list comprehension
first_names = [name.split()[0] for name in full_names]
last_names = [name.split()[1] for name in full_names]

print("First names:", first_names)
print("Last names:", last_names)

#Output
#First names: ['steve', 'bill', 'john', 'tim']
#Last names: ['jobs', 'gates', 'doe', 'cook']


## 2.list of words starting with "p"
# sentence = " Python is a programming language"
# new_sen=[char for char in sentence if char in 'pP']
# print(new_sen,'')
#Output--['P', 'p']
#var_name=[Tesp<if condition><else>Fexp<for condition>]
##3.list of elements if the element is a string reverse it else keep it as is
#USING FOR LOOP
items = ["hello", 12, "python", True, 12.1]
# new_item=[]
# for ele in items:
#     if type(ele)==str:
#         new_item.append((ele)[::-1])
#     else:
#         new_item.append(ele)
# print(new_item)
#Out put using for loop-['olleh', 12, 'nohtyp', True, 12.1]
#USING COMPREHENSION
new_item=[ele[::-1] if type(ele)==str else ele for ele in items ]
print(new_item)
#Output--['olleh', 12, 'nohtyp', True, 12.1]

##4.Filtering out those names which are less than 6 characters
# names = ['laura','stevs_jobs','bill_gates','james_doe','bob','greig','scott','alex','ive']
# new_name=[name for name in names if len(name)<6]
# print(new_name)

#Output--['laura', 'bob', 'greig', 'scott', 'alex', 'ive']