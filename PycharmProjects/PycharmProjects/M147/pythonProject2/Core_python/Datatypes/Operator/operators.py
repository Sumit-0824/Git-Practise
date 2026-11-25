# Operators:
# Operators are the special symbols which are used to do some specific operations
# All the operator are library functions
# whenever we want to perform any operation we require two things
#   operator
#   operand

# Types of operators:
# 1)Arithmetic operators
# 2)Logical operators
# 3)Bitwise operators
# 4)Assignment operators
# 5)Relational operators
# 6)Membership operators
# 7)Identity operators

# 1)Arithmetic operators :Arithmetic operators are used to perform mathematical operations
# # like addition, subtraction, multiplication and division

#Addition  '+'
print("**************Addition concept*****************")
print(20+5)                #25
print(20+5.5)              #25.5
print(20+5.5+3j)           #25.5+3j
print(20+True)             #21
print(20+False)            #20
print('20'+'10')           # 2010concatenation for string
print('20'+'[10,20,30]')   #20[10,20,30]
print([2,4,8]+[1,3,5])     #[2, 4, 8, 1, 3, 5]
print((2,4,8)+(1,3,5))     #(2, 4, 8, 1, 3, 5)
#print({2,4,8}+{1,3,5})    #it will return the base element
#print({2,4,8}+{2,4,5})
#print({'Bangalore': 25, “goa": 35, “punjab": 30}-{'pune': 44, “mysore": 35, “Patna": 30})

#It will not work for set and dictionary



#substraction  '-'
print("**************Substraction concept*****************")
print(20-5)
print(20-5.5)
print(20-5.5+3j)
print(20-True)
print(20-False)
#print('20'-'10')   #error
#print([2,4,8]-[1,3,5])#error
#print((2,4,8)-(1,3,5))#error
print({2,4,8}-{1,3,5})   #it will return the base element
print({2,4,8}-{2,4,5})   #It will return the unique element from the 1st value.It will consider 1st operand as base element and compare
#print({'Bangalore': 25, “goa": 35, “punjab": 30}-{'pune': 44, “mysore": 35, “Patna": 30})


#It will work for single data type and set in case of multiple data type
print("**********Multiplication concept**************")
#3.Multiplication   '*'

print(20*5)                  #100
print(20*5.5)                #110
print(20*5.5+3j)             #110+3j
print(20*True)               #20
print(20*False)               #0
#print('20'*'10')   #error
#print([2,4,8]*[1,3,5])#error
#print((2,4,8)*(1,3,5))  # error
#print({2,4,8}*{1,3,5}) #error
#print({'Bangalore': 25, “goa": 35, “punjab": 30}*{'pune': 44, “mysore": 35, “Patna": 30})  #error
#It will work only for single data types
#It will work by replication for string,list and tuple
print('hi'*4)                 #hihihihi
print([1,2,3]*3)              #[1, 2, 3, 1, 2, 3, 1, 2, 3]
print((1,2,3)*3)              #(1, 2, 3, 1, 2, 3, 1, 2, 3)

print("**********Division concept**************")
#4.Division
#true division(/)--float----23/4=5.75
#floar division(//--int-----23//4=5
#modulus(%)    23%4= 3 remainder
#It will work for only single value data type



print("**********Power concept**************")
#Power(**)
print(2**5)            #32
print(2**5.5)          #
print(2**5.5+3j)       #(45.254833995939045+3j)
print(2**True)         #2
print(2**False)        #1
#it will work only for single value data types