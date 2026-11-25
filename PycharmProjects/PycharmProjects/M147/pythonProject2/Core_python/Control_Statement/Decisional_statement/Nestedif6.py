# nested if:writing an if statement inside one more if statement is called nested if.
# when the 1st condition is mandatory to execute the 2nd condition

# syntax:
'''
if <condition>:
    if <condition>:
        TSB
    else:
        FSB
else:
    FSB
        '''
# WAPT find the second greatest number among a three number
a,b,c = 34,21,78
if a>b and a>c:
    if b>c:
        print(f'a->{b} is the second greatest number')
    else:
        print(f'a->{c} is the second greatest number')
elif b>a and b>c:
    if a>c:
        print(f'b->{a} is the second greatest number')
    else:
        print(f'b->{c} is the second greatest number')
else:
    if a>b:
        print(f'c->{a} is the second greatest number')  #Output
    else:
        print(f'c->{b} is the second greatest number')
##output---c->34 is the second greatest number
# wapt find middle element is even or odd

s = [3,4,5,7,9,1]

if len(s)%2!=0:
    m = s[len(s)//2]
    if m%2==0:
        print('even')
    else:
        print('odd')
else:
    print("as a machine i can't do this")
#output--as a machine i can't do this
#WAP to find second smallest number among three numbers.
a, b, c = 45, 65, 87
if a<b and a<c:
    if b<c:
        print(f'a->{b} is the second smallest number')   #output
    else:
        print(f'a->{c} is the second smallest number')
elif b<a and b<c:
    if a<c:
        print(f'b->{a} is the second smallest number')
    else:
        print(f'b->{c} is the second smallest number')
else:
    if a<b:
        print(f'c->{a} is the second smallest number')
    else:
        print(f'c->{b} is the second smallest number')

#a->65 is the second smallest number

#To find the second greater or second smallest among 3 to 4 number is easy but when we consider more than 4 number it is bit difficult to write the program by using nested if or nested elif

#To overcome above problem we use sort() function ,which will sort the collection in ascending order. So that we can easily access the required number from the collection.
