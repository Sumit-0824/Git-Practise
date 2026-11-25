#Datatypes:
#It is used to specify the type and size of the value present
#inside the Variable
#based on the size 2 type
#1 single value data type
#         -integer(int)
#         -float
#          -Complex
#           -boolean(bool)
#2 collection/multi value data types
#          -String
#          -list
#          -tuple
#          -set
#          -Dictionsry(dict

a=89
b=23,4,5

print(type(a))
print(type(b))

#Single value datatype
# 1.Integer:It is real number without a decimal points
#both +ve and -ve value
#We cannot check the length for single value data types
a=45  #non default data types
b=-34 #non default data types
c=0  #default data types
print(type(a))
print(type(b))
#print(len(a)) #Not possible

# 2float:It is real number with adecimal points
#both +ve and -ve value
a=3.4
b=-9.7
c=0.0
print(type(a))
print(type(b))
#print(len(a))   #Not possible
#Complex :The number which consist of both real and imaginary part
#a+bj or aj+b or bj
#a,b--->real number
#j---->Imaginary part

a=4j+8
b=3-7j
c=8j
#d=0j----> Default value
print(type(a))
print(type(b))
#4.Boolean(bool):True--->1,False--->0
a=True
b=False
#Both are assigning and non default
# = -->assignment operator
#==--->equal too operator
print(a==1)  #--->True
print(a==4)  #--->False






