# set:- Set is a collection of homogenous data item or heterogeneous data item which is
#  enclosed between the pair of flower brackets {}.
# - The values should be immutable i.e.,(int, float, complex,bool, string, tuple).
# - set is mutable datatype
# - Set is unordered in nature (the values will not be stored in a same order like
# how the user have given).
#  In set duplicated values will get eliminated.
# - Indexing is not possible in set collection because of its unordered nature.

l = []
print(type(l))    #list

t = ()
print(type(t))     #tuple

s = set()         # empty set
print(type(s))    #set

s1 = {23,4.5,True,7+9j,'hello',(11,22,44),4.5,23}
print(type(s1))      #set
print(s1)            #{True, (7+9j), (11, 22, 44), 4.5, 23, 'hello'}
print(len(s1))       #6
# unhashable -> mutable
# hashable -> immutable
print(hex(id(s1)))     #0x28231809b60

print(dir(set))

s = set()
s.add(34)
s.add(True)
s.add('hello')
#s.add([23,45,67])     #TypeError: unhashable type: 'list'

s.update([23,45,6766,55])
print(s)     #duplicate will be eliminated....23 is eliminated

# pop
#It removes the last value
print(s.pop())
print(s)      #{34, 'hello', 45, 6766, 55, 23}---->unordered
# remove
#It removes the particular value
s.remove('hello')
print(s)      #{34, 45, 6766, 55, 23}------->unordered

# clear
s.clear()
print(s)        #set()


#Method in string--->
#Methods in list---->append,extend,insert,count,index,reverse,sort,pop,remove,clear
#Method in tuple----->count,index
#Method in set---->add,pop,remove,clear
#Methods in dictionary--->get,update,items,keys,values




#Difference between tuple and set
#1.Tuple is immutable whereas set is mutable.
#2. Tuple is ordered whereas set is unordered in nature.
#3.Tuple has fixed memory whereas set is Variable memory.
#4.Indexing and slicing can be done is tuple whereas in set it cannot be done.
#5.Duplication of data is allowed in tuple whereas set support unique data.
#6.Tuple is having () as boundary whereas set is having {} as boundary.
#7.Tuple will store all kind of data whereas set will store immutable data


#Difference between list and set
#1. List is ordered whereas set is unordered in nature.
#2. List  has more methods compared to set.
#3.Indexing and slicing can be done is list whereas in set it cannot be done.
#4.Duplication of data is allowed in list whereas set support unique data
#5.list is having [] as boundary whereas set is having {} as boundary.
#6.Elements by their position can be accessed in list whereas Position access to elements is not allowed in set