###Enumerate and ZIP Concept##########

#ENUMERATE Concept#
# #Write a program to generate index and value pair
##output
'''
0 apple
1 orange
2 banana
3 strawberry
'''
#1st Method
fruits=['apple','orange','banana','strawberry']
for i in range(len(fruits)):  #traversing to generate list
    print(i,fruits[i])

#2nd method
#Enumerate-->Gives the data in index and the value pair
#in string form
for i,v in enumerate(fruits):
    print(i,v)
#in dictionary form
d={}
for i,v in enumerate(fruits):
    d[i]=v
print(d)
##output-->{0: 'apple', 1: 'orange', 2: 'banana', 3: 'strawberry'}

l = ['python.py', 'google.com', 'yahoo.in', 'file.txt' , 'file1.csv']
#in string form
# for i,v in enumerate(l):
#     print(i,v)

##output
'''
0 python.py
1 google.com
2 yahoo.in
3 file.txt
4 file1.csv
'''


#in dictionary form
# d={}
# for i,v in enumerate(l):
#     d[i]=v
# print(d)
##output-->{0: 'python.py', 1: 'google.com', 2: 'yahoo.in', 3: 'file.txt', 4: 'file1.csv'}

s = 'python java web selenium SQL manual C++ jscript'

d={}
words=s.split()
print(words)
#output-->['python', 'java', 'web', 'selenium', 'SQL', 'manual', 'C++', 'jscript']
for i,v in enumerate(words):
    d[i]=v
print(d)
#Output--{0: 'python', 1: 'java', 2: 'web', 3: 'selenium', 4: 'SQL', 5: 'manual', 6: 'C++', 7: 'jscript'}
###########ZIP CONCEPT############
# zip :Traverse through the collection parallelly
#1
a = [1,2,3,4]
b = [5,6,7,8]
c = [3,4,5,6,7,8,9]
# op:
# 1,5
# 2,6
# 3,4
# 4,8
for v1,v2 in zip(a,b):
    print(v1,v2)

for v1,v2,v3 in zip(a,b,c):
    print(v1,v2,v3)
#
'''
1 5 3
2 6 4
3 7 5
4 8 6
'''

a = [1,2,3]
b = ['x','y','z']
c = ['alpha','beta','gamma']
for x,y,z in zip(a,b,c):
    print(x,y,z)

##output
'''
1 x alpha
2 y beta
3 z gamma
'''



d1 = {'a':3,'b':4}
d2 = {'c':3,'d':7}
for v1,v2 in zip(d1.items(),d2.items()):
    print(v1,v2)
##output
'''
('a', 3) ('c', 3)
('b', 4) ('d', 7)
'''

cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai']
population = ['38,001,000', '25,703,168', '23,740,778', '21,066,245', '21,042,538']
for v1,v2 in zip(cities,population):

    print(v1,v2)
##output
'''
Tokyo 38,001,000
Delhi 25,703,168
Shanghai 23,740,778
Sao Paulo 21,066,245
Mumbai 21,042,538
'''

# d={}
# for v1,v2 in zip(cities,population):
#     d[v1]=v2
# print(d)

# {'Tokyo': '38,001,000', 'Delhi': '25,703,168', 'Shanghai': '23,740,778', 'Sao Paulo': '21,066,245', 'Mumbai': '21,042,538'}
