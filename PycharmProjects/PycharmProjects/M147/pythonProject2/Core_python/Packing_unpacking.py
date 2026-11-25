data=['IBM',50,91.1,(2019,7,17)]
name,share,prices,date= data

name,*_,(y,*_)= data


#######################################################################

# packing:it is  process of grouping an individual values in the form of collection
# to keep them securely

a = [2,3,4,5,6]

def display(*args):  # packing
    print(args)
display(1,2,3,4,5,)           #(1, 2, 3, 4, 5)

def display(**kwargs): #packing
    print(kwargs)                    #{'a': 4, 'b': 6}
display(a = 4,b = 6)

# unpacking
points = (5,6,7)
a,b,c = points            #a=5,b=6,c=7

data = ['IBM',50,91.1,(2019,7,17)]
name,share,prices,(y,m,d)= data  #or date   #name='IBM',share=50,prices=91.1 ,(y,m,d)=(2019,7,27)= date

names = ['apple','google','gmail','yahoo']
for i,v in enumerate(names):
    print(i,v)
'''
0 apple
1 google
2 gmail
3 yahoo
'''
#Packing
for i in enumerate(names):
    print(i)
'''   
(0, 'apple')
(1, 'google')
(2, 'gmail')
(3, 'yahoo')
'''

a = [1,2,3,4,5,6]
b = [9,8,7,6,5,5]
for v1,v2 in zip(a,b):
    print(v1,v2)
'''
1 9
2 8
3 7
4 6
5 5
6 5
'''
#UnPacking
temp = {'bangalore':(26,32),'chennai':(29,35),'delhi':(31,36)}
for city,(lowtemp,hightemp) in temp.items():
    print(city,lowtemp,hightemp)                     #Unpacking
'''
bangalore 26 32
chennai 29 35
delhi 31 36

'''
#Packing
temp = {'bangalore':(26,32),'chennai':(29,35),'delhi':(31,36)}
for v1 in temp.items():
    print(v1)
'''
('bangalore', (26, 32))
('chennai', (29, 35))
('delhi', (31, 36))
'''
s = {1,2,3,4,5,6,7,8}
f,*_,l = s         #Extracting first and last number
_,_,t,f,*_ = s     #Extracting 3,4 number
###Go to python console ----to access the data give _ not *_

data = ['IBM',50,91.1,(2019,7,17)]
name,*_,(y,*_) = data

def display(*args):  #
    print(args)      #packing  #(2, 3, 4, 5, 6)
    print(*args)   # unpacking

display(2,3,4,5,6)    #2 3 4 5 6  # unpacking
