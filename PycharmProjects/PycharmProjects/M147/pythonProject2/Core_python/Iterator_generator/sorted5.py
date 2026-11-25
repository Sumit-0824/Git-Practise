items = [[2,7],[7,3],[3,8],[8,7],[9,7],[4,9]]
#print(sorted(items,key=lambda ele:ele[0]))  ##Output--[[2, 7], [3, 8], [4, 9], [7, 3], [8, 7], [9, 7]]
print(sorted(items,key= lambda l: l[1]))  #[[7, 3], [2, 7], [8, 7], [9, 7], [3, 8], [4, 9]]

names = ['steve jobs', 'bill gates', 'john doe', 'tim cook', 'laura turner', 'alex martin']
print(sorted(names,key=lambda name: name.split()[1] ))   #['tim cook', 'john doe', 'bill gates', 'steve jobs', 'alex martin', 'laura turner']


portfolio = [ {'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}, {'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'ACME', 'shares': 75, 'price': 115.65} ]
print(sorted(portfolio,key=lambda d:d['price']))  #[{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}, {'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'AAPL', 'shares': 50, 'price': 543.22}]
print(sorted(portfolio,key=lambda d:d['shares'])) #[{'name': 'HPQ', 'shares': 35, 'price': 31.75}, {'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'FB', 'shares': 200, 'price': 21.09}]



#find the longest sub-string in the below string
sentence = "This is a Programming language and Programming is fun"


# def longest_word_sequence(sentence):
#     words = sentence.split()
#     longest_substr = ""
#
#     for word in words:
#         if len(word) > len(longest_substr):
#             longest_substr = word
#
#     return longest_substr
#
#
# sentence = "This is a Programming language and Programming is fun"
# result = longest_word_sequence(sentence)
# print("Longest word:", result)


print(sorted(sentence.split(),key=len)[-1])

#find the longest non repeating sub-string in the below string
sentence = "This is a Programming language and Programming is fun"
res= filter(lambda ele :sentence.count(ele)==1,sentence.split())
print(sorted(res,key=len)[-1])    #language#


###############Class  notes
# SORTTED :  new list containing all items from the iterable in ascending order
# it will work for all the datatype(list,tuple,dict,str,set)

names = ['apple','google','yahoo','amazon','facebook','microsoft','zomato']

prices = {'ACME':45.23,'AAPL':612.78,'IBM':205.55,'HPQ':37.20,'FB':10.75}

numbers = (2,3,4,5,6,7,1,8,9)

print(sorted(names))  #['amazon', 'apple', 'facebook', 'google', 'microsoft', 'yahoo', 'zomato']
print(sorted(names,reverse=True)) #['zomato', 'yahoo', 'microsoft', 'google', 'facebook', 'apple', 'amazon']
print(sorted(numbers,reverse=True)) #[9, 8, 7, 6, 5, 4, 3, 2, 1]


print(sorted(prices.items())) #[('AAPL', 612.78), ('ACME', 45.23), ('FB', 10.75), ('HPQ', 37.2), ('IBM', 205.55)]
# print(sorted('hello'))

# custom sorting
names = ['apple','google','yahoo','amazon','facebook','microsoft','zomato']
print(sorted(names,key = len))
print(sorted(names,key = len,reverse=True))

l = ['dc','wt','as']
print(sorted(l,key = lambda i: i[-1]))  ##['dc', 'as', 'wt']

temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]
print(sorted(temperatures))       #[('Bangalore', 25), ('Chennai', 37), ('Delhi', 35), ('Mumbai', 32)]
print(sorted(temperatures,key = lambda ele : ele[1] )) #[('Bangalore', 25), ('Mumbai', 32), ('Delhi', 35), ('Chennai', 37)]


items = [[2,7],[7,3],[3,8],[8,7],[9,7],[4,9]]
print(sorted(items, key = lambda l : l[1]))  #[[7, 3], [2, 7], [8, 7], [9, 7], [3, 8], [4, 9]]

print(sorted(items)) #[[2, 7], [3, 8], [4, 9], [7, 3], [8, 7], [9, 7]]

prices = {'ACME':45.23,'AAPL':612.78,'IBM':205.55,'HPQ':37.20,'FB':10.75}
print(sorted(prices.items(),key=lambda i:i[1])) #[('FB', 10.75), ('HPQ', 37.2), ('ACME', 45.23), ('IBM', 205.55), ('AAPL', 612.78)]


names = ['steve jobs', 'bill gates', 'john doe', 'tim cook', 'laura turner', 'alex martin']
print(sorted(names,key =lambda i:i.split()[1])) #['tim cook', 'john doe', 'bill gates', 'steve jobs', 'alex martin', 'laura turner']


students = [
    {"name": "john", "grade": "A", "age": 26},
    {"name": "jane", "grade": "c", "age": 28},
    {"name": "dave", "grade": "B", "age": 22}
]
print(sorted(students,key = lambda d :d['age'] )) #[{'name': 'dave', 'grade': 'B', 'age': 22}, {'name': 'john', 'grade': 'A', 'age': 26}, {'name': 'jane', 'grade': 'c', 'age': 28}]


portfolio = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]

#find the longest  sub-string in the below string
sentence = "This is a Programming language and Programming is fun"
print(sorted(sentence.split(),key = len)[-1])

#find the longest non repeating sub-string in the below string
sentence = "This is a Programming language and Programming is fun"
res = filter(lambda ele: sentence.count(ele)==1 ,sentence.split())
print(sorted(res,key=len)[-1])

#find the most repeted word in the below string
sentence = "hi hello hi hello world hi universe hi world hello world hi world"
d = {ele:sentence.count(ele) for ele in sentence.split()}
print(sorted(d.items(),key = lambda i : i[1])[-1][0])

#find the most repeted charater in the below string
sentence = 'hi hello hi hi hiiiiii'



sentence = "hi hello hi hello world hi universe hi world hello world hi world"

