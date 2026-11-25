#Generator expression:
#it is phenomenon of creating a new o/p collection by
# reducing the number of instrution taken to do the required operation.
#Generator expression can be done only for mutable collection-List,Set and Dictionary
# Generator expression is classified into 3 type:
# list expression
# set expression
# dict expression

# Generator  : it is phenomenon of creating a new list collection by
# reducing the number of instruction
#IMPORTANT
#For loop without any condition-# var_name = (expression <for loop>)
#For loop without with condition-# var_name = (expression <for loop> <if condition>)
#For loop with if and else statement-# var_name = (Texp <if condition> <else> Fexp <for loop>)

#difference with respect to expression----()
# typecast to the required collection
#next is same- we will get singe result in 1 call

# generator function that produces even number
a =[2,4,3,5,6,1,7,8,9,2,3]
even = (i for i in a if i%2==0)

#print(list(even))
#print(next(even))---------- 2 We will get single result in 1 call. for multiple we need to call multiple time
#output-[2,4,6,8,2]
#2.Generator function which yields the name starting with vowel
lst=['laura','anna','bill','steve','alex','ive','james','scott']

#Expression
vowel=(i for i in lst if i[0] in 'aeiouAEIOU')
#print(tuple(vowel))  #('alex', 'anna', 'ive')
#print(set(vowel))      #{'alex', 'anna', 'ive'}
print(list(vowel))      #['anna', 'alex', 'ive']

#3.build a list of tuple with string and its length pair
names = ['apple','google','yahoo','facebook','yelp','flipkart','gmail','microsoft']
n=((name,len(name)) for name in names )
#print(list(n))       #[('apple', 5), ('google', 6), ('yahoo', 5), ('facebook', 8), ('yelp', 4), ('flipkart', 8), ('gmail', 5), ('microsoft', 9)]


print(next(n))   #('apple', 5)-- By using next we will get result for individual data
#Reverse the item of the list if the item is of odd length string
names = ['apple','google','yahoo','facebook','yelp','flipchart','gmail','microsoft']
odd_string= (name[::-1] for name in names if len(name)%2!=0)
print(list(odd_string))   #['elppa', 'oohay', 'trahcpilf', 'liamg', 'tfosorcim']

'''
DRAW BACK:
1. assignment operators cannot be used
2. loop control statements cannot be used
3. elif statements can't be used
4. yield we cannot use inside the expression

'''
