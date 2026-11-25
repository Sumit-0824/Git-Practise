# elif:when ever we have multiple condition to check and condition having its own True
# statement block to execute we have to use if elif

'''
syntax:
if <condition>:
    TSB
elif  <condition>:
    TSB
elif <condition>:
    TSB
.
.
else:
    FSB
'''

# #  1WAP to check which is the smallest value among 3 numbers.
# a,b,c = 56,23,7
# if a<b and a<c:
#     print(f'{a} is smallest number')
# elif b<a and b<c:
#     print(f'{b} is smallest number')
# else:
#     print(f'{c} is smallest number')
#
#
# #2,WAP to check which is the largest value among 4 number
# a,b,c,d=34,21,56,2
# if a>b and a>c and a>d:
#     print(f'{a} is the largest number')
# elif b>a and b>c and b>d:
#     print(f'{b} is the largest number')
# elif c>b and c>b and c>d:
#     print(f'{c} is the largest number')
# else:
#     print(f'{d} is the the largest number')

#3 WAP to check whether the number is negative or neutral or positive.
num= int(input("Enter the number: "))
if num <0:
    print(f'{num} is negative')
elif num==0:
    print(f'{num} is neutral')
else:
    print(f'{num} is positive')