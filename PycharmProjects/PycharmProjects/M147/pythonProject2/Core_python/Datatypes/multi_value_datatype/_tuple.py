#Class Assignment
names = ('apple','google',['gmail','microsoft'],'yahoo','TCS')

print(names[-2])#'yahoo'
print(names[2][-1])#'microsoft'
t = ('hello','hai',(87,'hi',98),65)
print(names[2][1]) #'microsoft'
print(t[2][0])     #'hello'
print(t[1])        #'hai'
65
#immutable
#A=[12,34,56,78] print(A[1:4:1]) #print(A[1:5:1])-- output is same as 1st one Jan 6, 7:30 AM


#Var_name[si:ei:step value]
a = (12,34,56,78)
print(a[1:4:1])
print(a[::-2])
print(a[-2::-1])
a = ('hai',[1,2,3,'hello'])
print(a[1][3][::-1])
print(a[::-1])
print(a[0][1::1])


print("*******************class Notes****************")
# tuple is collection of homogeneous and heterogeneous element separated by comma.
# - Boundary :(...)
# - Element in tuple are ordered.
# - It allows duplicate elements.
# - It is  im-mutable datatype.
# int,float,complex,bool,str,dict,tuple
t = ()
print(type(t))  #<class 'tuple'>
t1 = (12,34,56,788,90)
t2 = ('apple','yahoo','google','yahoo')
t3 = (12, True,'hello',[12,3,4],(3,4,5))
print(t1) #(12,34,56,788,90)
print(t2) #('apple','yahoo','google','yahoo')
a = 12,34,56
print(type(a)) #<class 'tuple'>
print(a) #(12,34,56)
# -----------------------------------------------------------------------------
# indexing :
# var_name[index]
names = ('apple','google',['gmail','microsoft'],'yahoo','TCS')
print(names[-2])
t = ('hello','hai',(87,'hi',98),65)
print(t[2][0])     #87
print(t[1])        #hai
# print(t[4])  #error
# t[0] = 'anna'

# --------------------------------------------------------------------------------
# slicing a tuple
# var_name[start_index:end_index(+/-)1:step_value]
a = (12,34,56,78)
# 34,56,78
print(a[1::])
# 78,34
print(a[::-2])
# 56,34,12
print(a[-2::-1])

a = ('hai',[1,2,3,'hello'])
# 'olleh'
print(a[1][-1][::-1])
# [1,2,3,'hello'],hai
print(a[::-1])
# 'ai'
print(a[0][1::])

# ------------------------------------------------------------------------------------
# methods in tuple
print(dir(tuple))

names = ('apple','google','gmail','microsoft','yahoo','TCS','yahoo','yahoo','gmail')
print(names.count('yahoo'))
print(names.count('apple'))
print(names.count('gmail'))

print(names.index('gmail'))
print(names.index('apple'))




#Method in tuple----->count,index


#Difference between list and tuple

#list is mutable where as tuple is immutable
#list is having [] as boundary where as tuple is having() as boundary.
#list is having more method compared to tuple
#list is variable memory whereas tuple is fixed memory
























