# list:collection of homogeneous and hetrogenous element separated by comma.
# - Boundary :[…]
# int,float,complex,bool,str,tuple,set,dict,list
# - It is a mutable datatype.[we can modify,add new element and remove the element the original list]
# - Element in list are ordered.
# - It allows duplicate elements.


l = []
l1 = [12,34,56,78,90]
l2 = ['apple','google','yahoo','gmail','amazon','facebook']
l3 = [12,3.4,5+6j,'hi',True]
print(len(l2))
print(type(l3))
lst = ['hello','hi',['57',45,'hi'],9.8]

# ------------------------------------------------------------------------------
# indexing : the process of extracting single element from the list
# var_name[index]
#     -6      -5      -4       -3     -2          -1
# ['apple','google','yahoo','gmail','amazon','flipkart']
#     0       1        2       3       4         5

names = ['apple','google','yahoo','gmail','amazon','flipkart']
print(names[0])
print(names[-1])
print(names[-4])
# print(names[6])  #error

lst = ['hello','hi',['57',45,'hi'],9.8]
print(lst[1])
print(lst[2][1])
print(lst[2][2])
# print(len(lst))
# -----------------------------------------------------------------------------
# slicing:the process of extracting more than one element from the list
# var_name[startindex:endindex(+/-1):stepvalue]

names = ['apple','google','yahoo','gmail','amazon','flipkart']
print(names[::])
print(names[3::])
print(names[0:2+1:])
print(names[3:1-1:-1])
print(names[::2])
print(names[::-3])
# 'google','yahoo','gmail','amazon'
print(names[1:5:1])
# 'apple','google','yahoo','gmail'
print(names[0:4])
# 'flipkart','gmail','google'
print(names[::-2])
# -----------------------------------------------------------------------------
l = [12,34,56,78,90]
print(l)
l[0] = 23
print(l)
# s = 'hello'
# s[0] = 'o'

# ------------------------------------------------------------------------------------
print(dir(list))

l = [12,45]
l.append(23)
l.append(56)
# l.append([11,22])
l.extend([33,44,55])
print(l)

names = ['apple','google','yahoo','gmail','amazon','flipkart']
names.extend(['gmail','facebook','yahoo'])
print(names)

names.insert(3,'whatsapp')
print(names)

# count
print(names.count('yahoo'))
print(names.count('apple'))

# index
print(names.index('facebook'))
print(names.index('yahoo'))

print(names)

# reverse
# names.reverse()
# print(names)

# sort
names.sort()
print(names)
l.sort(reverse=True)
print(l)
# names.sort(reverse=True)
# print(names)
names.sort(key=len,reverse=True)
print(names)

# pop
print(names.pop())
print(names.pop(5))
print(names)

# remove
names.remove('google')
names.remove('flipkart')
# names.remove()
print(names)

# clear
names.clear()
print(names)

#Methods in list---->append,extend,insert,count,index,reverse,sort,pop,remove,clear