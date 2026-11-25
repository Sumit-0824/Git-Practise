#Position   2^5 2^4 2^3 2^2 2^1 2^0
#Value     32   16  8   4   2   0
#Ex  33    1    0   0   0   0   1
#33 and 45
#print(bin(33))     # 0b100001
#print(bin(45))     # 0b101101
#                ---------------
#
#                       100001
print(33&45)    #33

# --------------------------------------------------------------------------------
# bitwise operators:Those are the operator which will convert the given operand into
# binary value and it will perform bit by bit operation.
# 23 -->  binary value --> operator --> ans
# converting the int to binary number:(divied the given value by 2) bin()
#bin() :-is built in function it will return the binary value of argumemnt

# 1. bitwise and operator (&)
# 2. bitwise or operator (|)
# 3. bitwise not operator(~)
# 4. bitwise xor operator(^)
# 5. bitwise right shift(>>)
# 6. bitwise left shift(<<)
print("**************Bitwise and Operator****************")
# 1. bitwise and operator (&)
#Syntax op1 & op2
'''
op1     op2     o/p
0       0       0
0       1       0
1       0       0
1       1       1
'''

print(23 &34)

'''
23 --> 10111
34 -->100010
-------------
      000010
      '''
print(12 & 13)

'''
12 --> 1100
13 --> 1101
-----------
and -->1100    #12
or-->  1101    #13
'''

print(-5 and 2)   #2
'''
print(bin(-5))---0101
print(bin(2)-----0010
                 -----
#bin() :-is built in function it will return the binary value of argumemnt

'''
#Example33 and 45
#print(bin(33))     # 0b100001
#print(bin(45))     # 0b101101
#                ---------------
#                       100001
print(33&45)    #33
# Example7 and 4
print(7&4)  #  4
#print(bin(7)
'''
7--------0110
4--------0100
         -----
         0100---->4
'''
print("******************Bitwise or operator**********")

#2. bitwise or operator (Symbol- |)
#Syntax : op1 | op2
'''
op1     op2     o/p
0       0       0
0       1       1
1       0       1
1       1       1
'''
print(23 | 26)    #31
'''
23 -->10111
26 -->11010
-----------
      11111-31
'''

print(13|12)       #13
'''
12 --> 1100
13 --> 1101
------------
        1101----->13
'''
print(-5|2)        #-5
#print(bin(-5))---0101
#print(bin(2)-----0010
 #                -----  #-5
#bin() :-is built in function it will return the binary value of argumemnt --check with mam

print(-5|-2)  #-1
#print(bin(-5))---0101
#print(bin(-2)----0010



print("******************Not operator**********")

#3 bitwise not operator(~) : -(n+1)
#It is an operator which will return the positive o/p if thegiven i/p is negative and it will return -ve o/p if the givin operand is +ve.
#Syntax :- ~(op)
print(~34)   #-35  --->-(34+1)
print(~7)    #-8   --->-1(7+1)
#-ve o/p if the givin operand is +ve.
#-(op+1)
#To perform bitwise not operation
#-(op+1)
print(~-9)   #8    ----> (-9+1)

print("******************Bitwise xor operator**********")

#4.bitwise xor operator(^):
#It is an operator which will return as true if any one of i/p true or if both the i/p not equal else if will return false.



'''
op1     op2     o/p
0       0       0
0       1       1      True
1       0       1      True
1       1       0      False since operand are equal
'''
print(14 ^ 12)
'''
14 --> 1110
12 --> 1100
------------
       0010
'''


print(4^2)   #6
'''
4---->0100
2---->0010
-------------
       0110----> Ans 6
'''
print(8^3)
'''
8------>1100
3------>0010
--------------
        1110--------->Ans 11


'''

print("******************Bitwise right shift operator**********")



#5.bitwise right shift(symbol-  >>)
#It is an operator which will remove the number of bits from the right side of binary values based an the value for n specified by the user.
#Syntax : operand>>n
print(12>>2)
#print (bin(12))------1001---Shift the 2 bits from thr right side since n is 2
#left bit---10--->result-->2
#Value of bits.......32 16 8 4 2 1
print(13>>2)
#print (bin(13))------1101---Shift the 2 bits from thr right side since n is 2
#left bit---11--->result-->3
print(15>>2)
# 15----1111
#left shift---11-->3
print(19>>3)
#           10011
#shift 3 bits from the right----left bit--10----Ans-3
print(19>>2)
#           10011
#shift 2 bits from the right----left bit--100----Ans-4


print("******************Bitwise left shift operator**********")


# 6.bitwise left shift(Symbol-  <<):-It is an operator which is used to add the number of zeroes to rigtht side of a given binary value based on the specified value for n.
# Syntax :-operand<<n


print(9<<2)
#9-------------1001
#adding 2 bits on the right side 1 0 0 1  0  0
#Value of bits.......           32 16 8 4 2 1
#36

print(1<<2)
#1-------------0001
#adding 2 bits on the right side 0 0 0 1  0  0
#Value of bits.......           32 16 8 4 2 1
#4
print(7<<7)
#7-------------0111
#adding 7 bits on the right side 0 1 1 1  0  0 0 0 0 0 0
#Value of bits.......                     512  256 128 64 32 16 8 4 2 1
#896
print(5<<1)  #10