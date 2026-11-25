names = ['apple','google','yahoo','gmail','amazon','flipkart']
print(names[1:5:1])
print(names[1:-1:1])
print(names[ : :-2])




A=[12,34,56,78]
print(A[1:4:1])
#print(A[1:5:1])-- works same output as above

B=['hai',[1,2,3,'hello']]
print(B[1][3][::-1])               #olleh
print(B[1][::-1])                  #['hello', 3, 2, 1]
print(B[0][1:3:1])                 #ai


names=['apple','google','yahoo','amazon','facebook','instagram','microsoft']

print(names[-4:-2])                    # o/p------['amazon', 'facebook']
print(names[-6:5])                     #o/p-------['google', 'yahoo', 'amazon', 'facebook']
print(names[1:-1])                     #o/p-------['google', 'yahoo', 'amazon', 'facebook', 'instagram']
print(names[2:7:2])                    #o/p-------['yahoo', 'facebook', 'microsoft']

# Class assignment
#list Slicing
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# 1. Reverse the above list.
print(names[::-1])     #
## #['microsoft', 'instagram', 'facebook', 'amazon', 'yahoo', 'google', 'apple']
# 2. What is the output of names[2][3]
#0
# 3. What is the output of
# 	a. names[-2: 3]
print(names[-2:3])
#[]
# 	b. names[-6:5]
print(names[-6:5])
#['google', 'yahoo', 'amazon', 'facebook', 'instagram']
# 	c. names[-1:2:-1]
print(names[-1:2:-1])
#['microsoft', 'instagram', 'facebook', 'amazon']
# 	d. names[13]
#print(names[13])  #list index out of range
# 	e. names[:2] = ['unknown', 'Unknown']
names[:2] = ['unknown', 'Unknown']
print(names)
#['unknown', 'Unknown', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']


# Methods in list
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook','instagram','microsoft']

# 	1. What is the output of:
# 			a. names.append(['netflix', 'walmart', 'kroger’])
#names.append(['netflix', 'walmart','kroger'])
#print(names)
#['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', ['netflix', 'walmart', 'kroger']]

# 			b. names.extend(['netflix', 'walmart', 'kroger'])
names.extend(['netflix', 'walmart','kroger'])
print(names)
#['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'netflix', 'walmart', 'kroger']

# 	2. What is the difference between pop, remove.
#Ans--->pop-erase the remove the element from the collection and return where as by using remove method we can remove the particular element from collection by giving particular index

# 	3. Sort the above list in descending order.
print(names.sort())
# 	4. Sort the above list in ascending order according to their length.
names.sort(key=len)      #reverse not required
print(names)

# 	5. Sort the above list in descending order according to their length.
names.sort(key=len,reverse=True)
print(names)

# 	6.string = "Hi welcome to python"
# 		a. Create a list with each character of the string as its element.
# 		o/p ['h','i',' ' ,'w'.....]
string = "Hi welcome to python"
print(list(string))                #['H', 'i', ' ', 'w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n']

#         b. Create a list with each word of the string as its element.
print(string.split())
#Ans--->['Hi', 'welcome', 'to', 'python']
#         o/p ['hi','welcome','to','python']
