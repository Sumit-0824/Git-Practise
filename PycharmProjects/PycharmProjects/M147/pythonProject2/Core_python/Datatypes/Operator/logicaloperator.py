# 2)Logical operators:and,or,not
# 0 -- > False
# 1 --> True
# and
'''
op1     op2     o/p
0       0       0
0       1       0
1       0       0
1       1       1
'''
'''
op1 --> True   o/p op2
op1 --> False  o/p op1
Ex-12 and 13 --------->13
Ex-0 and set()--------->0
Ex-23 and set()-------->set()
Ex-{} and 0.0----------->{}
Ex--
if23 and 56 and 75
1. 23 and 56--->23
2.23 and 75---->23

'''
# Default values like 0,0.0,0j,False,'',[],(),set(),{}  --> false
# or
'''
op1     op2     o/p
0       0       0
0       1       1
1       0       1
1       1       1
'''
'''
op1 --> False  o/p -> op2
op1  -->True  o/p -> op1

Example
if 3>5 or 6>4   ---> both are true  o/p- op1
if 3>2 or 6>4   ---> both are true  o/p- op2
if23 or 56 or 75
1. 23 or 56--23
2.23 or 75---->23

Ex-{2,3,4} or set()----->{2,3,4}
Ex-{} or 0------>           0
Ex-{}  or ''---->           ' '


'''
# not

# op1  o/p
# 0     1
# 1     0
not(True)  #---->>False
not(False) #----->>True
not(45)    #False
not(0)     #0

#Assignment operator

a= 67
l= [12,34,67]
a = a+5
#a += 5
print(a)
