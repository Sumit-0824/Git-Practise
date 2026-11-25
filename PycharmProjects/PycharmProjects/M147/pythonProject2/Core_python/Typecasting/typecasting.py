#Type casting:It is a phenomenom of converting one data type into another data type based on the user requirement
#1.Int
A=10
# print(float(A))                               #10.0
# print(complex(A))                             #(10+0j)
# print(bool(A))                                #True
# print(str(A))                                 #10
# #print(list(A))                               #TypeError: 'int' object is not iterable
# #print(tuple(A))                              #TypeError: 'int' object is not iterable
# #print(set(A))                                #TypeError: 'int' object is not iterable
# #print(dict(A))                               #TypeError: 'int' object is not iterable

#Int can be converted to all float,complex,bool and string


# #2.Float
# A=10.5
# print(int(A))                                 #10
# print(complex(A))                             #(10.5+0j)
# print(bool(A))                                #True
# print(str(A))                                 #10.5
# #print(list(A))                               #TypeError: 'int' object is not iterable
# #print(tuple(A))                              #TypeError: 'int' object is not iterable
# #print(set(A))                                #TypeError: 'int' object is not iterable
# #print(dict(A))                               #TypeError: 'int' object is not iterable

#Float can be converted to all Int,complex,bool and string

#3.complex
A= 5+7j


#print(int(A))                                #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#print(complex(A))                             #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#print(bool(A))                                #True
#print(str(A))                                 #(5+7j)
#print(list(A))                               #TypeError: 'int' object is not iterable
#print(tuple(A))                              #TypeError: 'int' object is not iterable
#print(set(A))                                #TypeError: 'int' object is not iterable
#print(dict(A))                               #TypeError: 'int' object is not iterable
#print(int(5+7j))        #int() argument must be a string
#print(float(5+7j))     #float() argument must be a string or a real number, not 'complex'
#print(bool(5+7j))       #True

#Complex can be converted into bool and string data type.
##4.Bool
A= True

print(int(A))                                 #1
print(complex(A))                             #(1+0j)
print(float(A))                               #1.0
print(str(A))                                 #True
#print(list(A))                                #TypeError: 'bool' object is not iterable
#print(tuple(A))                              #TypeError: 'int' object is not iterable
#print(set(A))                                #TypeError: 'int' object is not iterable
#print(dict(A))                               +#TypeError: 'bool' object is not iterable

A= False

print(int(A))                                 #0
print(complex(A))                             #0j
print(float(A))                               #0.0
print(str(A))                                 #False
#print(list(A))                                #TypeError: 'bool' object is not iterable
#print(tuple(A))                              #TypeError: 'int' object is not iterable
#print(set(A))                                #TypeError: 'int' object is not iterable
#print(dict(A))                               +#TypeError: 'bool' object is not iterable

#Bool can be converted to single data type and string in multi data types

#String conversion
s= 'hello'
#print(int('hello'))        #ValueError: invalid literal for int() with base 10
#print(float('hello'))      #ValueError: invalid literal for int() with base 10
#print(complex('hello'))    #ValueError: complex() arg is a malformed string
#print(bool('hello'))        #True
#print(list('hello'))        #['h', 'e', 'l', 'l', 'o']
#print(tuple('hello'))        #('h', 'e', 'l', 'l', 'o')
#print(set('hello'))          #{'l', 'o', 'h', 'e'}
#print(dict('hello'))         #ValueError: dictionary update sequence element #0 has length 1; 2 is required

#in case of character Typecasting will work for bool,list,tuple and set.
#in case of character Typecasting will not work for int,float,complex and dict.
#s1 =123
# print(int(s1))             #123
# print(float(s1))        #123.0
# print(complex(s1))     #(123+0j)
# print(bool(s1))        #True
#print(list(s1))        #TypeError: 'int' object is not iterable
# #print(tuple(s1))        #TypeError: 'int' object is not iterable
# #print(set(s1))          #TypeError: 'int' object is not iterable
# print(dict(s1))         #ValueError: dictionary update sequence element #0 has length 1; 2 is required

#A string datatype can be type casted into all single value datatype (int, float, complex) only if the sting values are numbers other than numeric values if string contains any other character it gives error.
#Since the values in a dictionary are stored key : value pair a string cannot be type casted into dictionary data type


#list

l=[11,22,33,44,55,66,77]

#print(int(l))             #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
#print(float(l))           #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
#print(complex(l))          #complex() first argument must be a string or a number, not 'list'
print(bool(l))            #True
print(str(l))              #[11, 22, 33, 44, 55, 66, 77]
print(tuple(l))            #(11, 22, 33, 44, 55, 66, 77)
print(set(l))              #{33, 66, 11, 44, 77, 22, 55}  -->unordered
#print(dict(l))         #ValueError: dictionary update sequence element #0 has length 1; 2 is required

#Typecasting will work for string,tuple,set.
#Typecasting will not work for int,float,complex,dict


print("***********************Tuple concept**************")
#tuple
t=(12,34,56,78,90)

#print(int(t))           #error
#print(float(t))          #error
#print(complex(t))        #error
print(bool(t))            #True
print(str(t))              #(12, 34, 56, 78, 90)
print(list(t))             #[12, 34, 56, 78, 90]
#print(set(t))              #{34, 12, 78, 56, 90}-----unordered
#print(dict(t))             #TypeError: cannot convert dictionary update sequence element #0 to a sequence

#Tuple It will work for bool,str,list,set
#Tuple will not work for int,float,complex and dictionary
print("***********************Set concept*********************")
s={12,34,56,78,90}

#print(int(s))           #error
#print(float(s))          #error
#print(complex(s))        #error
print(bool(s))            #True
print(str(s))              #{34, 56, 90, 12, 78}-----unordered
print(list(s))             #[34, 56, 90, 12, 78]-----unordered
print(set(s))              #{34, 56, 90, 12, 78}-----unordered
#print(dict(s))             #TypeError: cannot convert dictionary update sequence element #0 to a sequence

#set It will work for bool,str,list,set
#set will not work for int,float,complex and dictionary

print("***********************dict concept*********************")
d={1:2,3:4,5:6,7:8,9:1}

#print(int(d))           #error
#print(float(d))          #error
#print(complex(d))        #error
print(bool(d))            #True
print(str(d))              #{1: 2, 3: 4, 5: 6, 7: 8, 9: 1}-----unordered
print(list(d))             #[1, 3, 5, 7, 9]-----It will give the key
print(set(d))              #{1, 3, 5, 7, 9}}-----It will give the key
#in case of dict if we convert into other datatype we will get only keys because in dict for the control the visible layer is key layer
