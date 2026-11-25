# # Generator: it is a function that returns an iterator_object
# # 'yield'--> return the value,and it will pause the execution
# '''
# def func_name(args):
#     statement block
#     yield value
#
# var_name = func_name(args)
# # typecasting or next or for loop
# '''

#Return-returns the value  and comeout of function
#Yield-It will the pause the execution
# We should avoid type casting when ever we have more than 1 yield option. We should use  for loop and other function
#next(): This method returns the next element in the sequence.
# Once all elements are consumed, it typically raises a StopIteration exception to signal the end of the iteration.
def func():
    return 30
    return 20
print(func()) #30
# it will give result 30 and will not go to 2nd
def func1():
    yield 30
    yield 20

#print(func1())   #only 1 we will get output.
# a = func1()
# print(next(a))#30
# print(next(a))#20

def func():
    print('hello')
    yield 'hi'
    print('world')
    yield 'bye'

s = func()
# for i in s:
#     print(i)
#print(list(s)) #It will give all hello, world
#['hi', 'bye']

#print(next(s))
#print(next(s))   #hello,hi

# generator function that produces even number
def evens(coll):
    print('generator function')
    for ele in coll:
        if ele%2==0:
            yield ele
            print('after the generator function')
e = evens([2,4,3,5,6,1,7,8,9,2,3])
#print(list(e))  #[2,4,6,8,2]
print(next(e))
print(next(e))


# 1.generator function that produces even number print(next(e))
# def evens(coll):
#     print('generator function')
#     for ele in coll:#2nd method
# # print(next(e))
# # print(next(e))
# # print(next(e))
# #2.Generator function which yields the name starting with vowel
# lst=['laura','anna','bill','steve','alex','ive','james','scott']
#
# def vowel(lst):
#     for i in lst:
#         if ele%2==0:
#             yield ele
#             print('after the generator function')
# e = evens([2,4,3,5,6,1,7,8,9,2,3])
#1stt method
# # # print(list(e))
#         if i[0] in 'aeiouAEIOU':
#             yield i
# print(list(vowel(['laura','anna','bill','steve','alex','ive','james','scott'])))   #['anna', 'alex', 'ive']
#3.WAPT to get the ASCII value of the lower case alphabet using yield
'Python'
def lower(s):
    for char in s:
        #if char.islower():
        if char >='a' and char <='z':  #put the char ''- it is string
            yield ord(char)            # ord
a=lower('Python')
print(list(a)) #[121, 116, 104, 111, 110]

