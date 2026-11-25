# Membership operators:It is an operator which is used to check whether the given the value
# # is present inside the collection
# Membership operator got classified into 2 types
#     in operator
#     not in

# in operator(in) : it returns True if the given the value is present inside the
# collection else False
# it is used only for the collection datatype
print(34 in [12,34,56,78])  #True
print(34 in [12,23,56,78])  #False
# print(1 in 1234)
print('e' in 'hello')
print('d' in {'b':34,'c':22,'a':56})

# not in :it returns True if the given the value is not present inside the
# collection else False
print('l' not in 'hi')
print('i' not in 'hi')
print('d' not in {'b':34,'c':22,'a':56})
print('a' not in {'b':34,'c':22,'a':56})