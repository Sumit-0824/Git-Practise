# 1.strong number     #A number is called strong number if sum of the factorial of its digit is equal to number itself
#Example= 145= 1!+4!+5!
import math
num=100
#num= int(input('Enter the number: '))
n=num
res=0
while num>0:
    res=res+math.factorial(num%10)
    num=num//10
if n==res:
    print('Strong Number')
else:
    print('Not a strong Number')

#2. perfect number
# #In number theory, a perfect number is a positive integer that is equal to the sum of its posit
# ive proper divisors
#Example-6- 1+2+3, 28-1+2+4+7+14
# Input from the user
#num = int(input("Enter a number to check if it's a perfect number: "))
# num=6
# sum = 0
# div = 1
# while div < num:
#     if num % div == 0:
#         sum += div
#     div += 1
# if sum == num:
#     print(f"{num} is a perfect number.")
# else:
#     print(f"{num} is not a perfect number.")


num=6
sum=0

for i in range(1,(num//2),1):
    if num%1==0:
        sum=sum+i



#3. neon number--A neon number is a number where the sum of digits of square of the number is equal to the number.
# For example if the input number is 9, its square is 9*9 = 81 and sum of the digits is 9.
num=9
sum=0
Sq=num**2
while Sq>0:
    sum+=Sq%10
    Sq//=10
if sum == num:
    print(f"{num} is a neon number.")
else:
    print(f"{num} is not a neon number.")
#4. spy number
#A spy number is a number where the sum of its digits is equal to the product of its digits. For example, 112 is a spy number because:

#Sum of digits: 1 + 1 + 2 = 4
#Product of digits: 1 * 1 * 2 = 4
num=4
sum=0
product=1
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit
    product *= digit
    temp //= 10

if sum==product:
    print(f'{num} is a spy number')
else:
    print(f'{num} is not spy number')



# happy number
'''
A happy number is a number that eventually reaches 1 when you repeatedly replace the number by the sum of the squares of its digits. If a number is not happy, it will end up in a cycle that doesn't include 1.

For example:

19 is a happy number:
1² + 9² = 1 + 81 = 82
8² + 2² = 64 + 4 = 68
6² + 8² = 36 + 64 = 100
1² + 0² + 0² = 1 + 0 + 0 = 1 (so, 19 is a happy number).
'''
















#Armstrong number
'''
An Armstrong number (also known as a Narcissistic number or Pluperfect number) is a number that is equal to the sum of its own digits raised to the power of the number of digits.

For example:

153 is an Armstrong number because:
1³ + 5³ + 3³ = 1 + 125 + 27 = 153.
'''

# sunny number
'''
A sunny number is a number that is one less than a perfect square. In other words, if you add 1 to the number, the result should be a perfect square.

For example:

8 is a sunny number because 8 + 1 = 9, which is a perfect square (3² = 9).
'''
#num = int(input("Enter a number to check if it's a sunny number: "))
num=8
Second_num = num + 1
sqrt_Second_num = int(Second_num ** 0.5)
if sqrt_Second_num * sqrt_Second_num == Second_num:
    print(f"{num} is a sunny number.")
else:
    print(f"{num} is not a sunny number.")











