# INTERMEDUATE TEMINATION IN LOOP/ LOOPING CONTROL STATEMENT
# when ever we want to terminate the loop in b/w ,we should make use:
# 1. break
# 2. continue
# 3. pass

# 1. break:
# for i in range(16):
#     print(i)
#     break
# print('python')

# WAPT to print initial index of a given charater present inside the given string
# st = 'hello'
# char = 'l'
# for i,v in enumerate(st):
#     if char ==v:
#         print(i)
#         break

# WAPT run the loop continuously until user enter the proper password
# password = 'pysp112'
# while True:
#     pwd = input('enter the password:')
#     if pwd == password:
#         print('login')
#         break
#     else:
#         print('enter the correct password')

# WAPT guess the number
# n = 67
# while True:
#     num = int(input('enter the number:'))
#     if n==num:
#         print('you guessed it!..')
#         break
#     elif num>n:
#         print('the guessed number is greater')
#     else:
#         print('the guessed number is lesser')


# 2. continue:used to skip the current execution and to make the control to go the next iteration

# for number  in range(1,11):
#     if number == 6 or number==9:
#         continue
#     print(number)

# WAPT TO traverse a collection if it get double digit skip that and continue the iteration
l = [3,7,6,34,5,6,12,7,1]
for i in l:
    if i>9:
        continue
    print(i)
# WAPT TO traverse a collection if it get double digit skip that and continue the iteration to add the single digit
# l = [3,7,6,34,5,6,12,7,1]
# res=0
# for i in l:
#     if i>9:
#         continue
#     res=res+i
# print(i)


# pass:used to make any empty statement block as valid block

# if 3>5:
#     pass
#
# for i in range(1,10):
#     pass