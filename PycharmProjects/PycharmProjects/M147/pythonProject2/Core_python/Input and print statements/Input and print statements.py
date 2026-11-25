# print() :
# It is a statement which is used to display the output on the screen.
# syntax:
# Print(any_number_arguments, sep = ' ' , end = '\n')
# sep:string inserted between values, default a space.
# end:string appended after the last value, default a newline.

# print(12,34,56,78,sep = '^',end = '$')
# print(2,3,4)



# input():In python, we make use of a function called input() to get the input from the user.
# The syntax used is :
# var_name = input('string')
# - The input which is taken by input statement will always be in the form of string type.
# - To get the required type value, typecasting is required.
# - We cannot take input for list, tuple, set and dictionary .- We use eval()
#By using type casting we can use input for int,float,complex and bool

# age = int(input('enter the age:'))
# print(type(age))
# print(age+5)

# num  = bool(input('enter the value:'))
# print(type(num))
# print(num)

# num = list(input('enter the values:'))
# print(type(num))
# print(num)

# eval():It will retain the type of data type provided by the user
#Meaning if user input is list it will give output as list.if set it will give output as set.
#eval() for list, tuple, set and dictionary
# The syntax used is :
# var_name = eval(input('string'))
a = eval(input('enter the value'))
print(type(a))
print(a)

