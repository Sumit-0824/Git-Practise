# iterable: __iter__ :list,str,range,tuple,set,dict
a = 234567
l = [1,2,3,4,5,6,7]
# all the iterator are iterable but all the iterable are not iterators
# iterator: __iter__,__next__ :enumerate,zip,reversed,generators,map,filter,fileobject,..

l = [12,34,56,78,90]
print(len(l))

e = enumerate(l)
# print(len(e))
# print(dir(e))

# '''
# for i in l:
#     print(i)
#
# 12
# 34
# 56
# 78
# 90
# for i in l:
#     print(i)
#
# 12
# 34
# 56
# 78
# 90
# for i in l:
#     print(i)
#
# 12
# 34
# 56
# 78
# 90
# for i in l:
#     print(i)
#
# 12
# 34
# 56
# 78
# 90
# for i in l:
#     print(i)
#
# 12
# 34
# 56
# 78
# 90
# for i in e:
#     print(i)
#
# (0, 12)
# (1, 34)
# (2, 56)
# (3, 78)
# (4, 90)
# for i in e:
#     print(i)
#
# for i in e:
#     print(i)
#
# for i in e:
#     print(i)
#
# e = enumerate(l)
# for i in e:
#     print(i)
#
# (0, 12)
# (1, 34)
# (2, 56)
# (3, 78)
# (4, 90)
# for i in e:
#     print(i)
#
# next
# <built-in function next>
# e = enumerate(l)
# next(e)
# (0, 12)
# next(e)
# (1, 34)
# next(e)
# (2, 56)
# for i in e:
#     print(i)
#
# (3, 78)
# (4, 90)
# next(e)
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2.5\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# StopIteration
# l
# [12, 34, 56, 78, 90]
# e
# <enumerate object at 0x00000214BD86F010>
# '''
#

#########Class practicse#################
t=(1,2,3,4,5,6)
print(len(t))


z=zip(t)
#print(len(z))---TypeError: object of type 'zip' has no len()

#Differences bethween iterator and iterable
'''
#length can be known for collection incase of iterable
#we can traverse again and again in iterable where as in case of iterator we cannot 
#iterable---__iter__ 
#iterator---__iter__ ,__next_
#All the iterator are iterable but all the iterator are not iterables.

'''
#_____________________________________________________________________________________________#
#