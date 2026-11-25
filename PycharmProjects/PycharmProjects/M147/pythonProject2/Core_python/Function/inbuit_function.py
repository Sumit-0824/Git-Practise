# # inbuilt function:
# '''
# len -->  length or number of element of the object
# id,hex -->memory address
# abs -->
# chr -->
# ord -->
# bin -->
# min -->
# max -->
# type -->
# isinstance
# range
# enumerate
# sum
# Counter
# zip
# '''



###list##
l=[12,34,56,78,22,11,88,99]
print(sum(l))  #400
print(max(l))  #99
print(min(l))  #11

###Tuple##
t=(12,34,56,78,22,11,88,99)
print(sum(t)) #400
print(max(t)) #99
print(min(t)) #11

##Set##
s={12,34,56,78,22,11,88,99}
# print(sum(s))  #400
# print(max(s))  #99
# print(min(s))  #11

##Dictionary##
d={1:2,3:4,5:6,7:8}
print(sum(d))   # Sum of key by default
print(max(d))   # Max of key by default
print(min(d))   # Min of key by default

print(sum(d.values()))  #20
print(max(d.values()))  #8
print(min(d.values()))  #2

##reversed##
#s= 'Sumit is in Python class'
#print(str(reversed(s)))
#print(list(reversed(l)))  #[99, 88, 11, 22, 78, 56, 34, 12]
#print(tuple(reversed(t))) #(99, 88, 11, 22, 78, 56, 34, 12)
#print(reversed(s))
#print(set(reversed(s)))
#print(dict(reversed(d)))
print(dict(reversed(d.items())))  #{7: 8, 5: 6, 3: 4, 1: 2}

#Reversing the string
k='hello'
print(''.join(list(reversed(k))))  #olleh-- We need to type cast to list then join ach character
print(k[::-1])     #olleh---It is adviced to use slicing


#  counter
from collections import Counter
sentence = 'hello world welcome to python hello hi world welcome to python'
print(Counter(sentence.split()))

#output-Counter({'hello': 2, 'world': 2, 'welcome': 2, 'to': 2, 'python': 2, 'hi': 1})
#enumerate--gives the index and value pair
#zip-Traverse through the collection parallelly

#ziplongest
a = [1,2,3]
b = ['x','y','z']
c = ['alpha','beta','gamma']

#1st method
import itertools
for x,y,z in itertools.zip_longest(a,b,c):
    print(x,y,z)
'''
1 x alpha
2 y beta
3 z gamma
'''
#2nd method
#import itertools
from itertools import zip_longest
for x,y,z in zip_longest(a,b,c):
    print(x,y,z)

'''
1 x alpha
2 y beta
3 z gamma
'''
#---------------------------------------------------------------------------------------------------------
# default dictionary:When ever we will do initializationa and updation simultaneouly we use it
from collections import defaultdict

# # default dictionary:
#
# d = {}
# string = 'aaaabbbbbbccd'
# # output: {'a':4 , 'b':6 , 'c':2 , 'd':1}
# d = {}
# for char in string:
#     if char in d:
#         d[char]+=1
#     else:
#         d[char] = 1
# print(d)
#
# # var_name = defaultdict(datatype)
# d1 = defaultdict(int)  # empty defaultdict
# for char in string:
#     d1[char] += 1
# print(d1)
#
# #WAPT to create a dict  as extension and file names in list pair
l = ['python.txt','notes.py','demo.txt','pic.img','string.py','list.txt',
     'python.exe','pycharm.exe']
# o/p{'txt':['python','demo','list'],'py':['notes','string'],'img':['pic']...}
l1 = defaultdict(list)
for ele in l:
    s = ele.split('.')
    l1[s[1]] += [s[0]]
print(l1)
#output---defaultdict(<class 'list'>, {'txt': ['python', 'demo', 'list'], 'py': ['notes', 'string'], 'img': ['pic'], 'exe': ['python', 'pycharm']})

l = ['amazon','facebook','twitter','youtube','apple','toy','fish','telephone','flipkart','yahoo']
# # o/p: {'a':['amazon','apple'],'f':['facebook','flipkart'],'t':[],....}

l1 = defaultdict(list)
for ele in l:
    l1[ele[0]] += [ele]
print(l1)
#defaultdict(<class 'list'>, {'a': ['amazon', 'apple'], 'f': ['facebook', 'fish', 'flipkart'], 't': ['twitter', 'toy', 'telephone'], 'y': ['youtube', 'yahoo']})
