# Identity operators:It is an operator which is used to check whether both the
# variable are pointing to the same memory location or not.
# Identity operator got classified into two types.
#     is
#     is not

# is : it returns True when both the variable are pointing to the same memory
# location else False.
a = 34
b = 67
c = 34
print(id(a))
print(id(b))
print(id(c))
print(a is c)
print(a is b)
l1 = [12,34,56]
l2 = [12,34,56]
l3 = l1
print(l1 is l2)
print(id(l1))
print(id(l2))
print(id(l3))
print(l1 is l3)

# is not:it returns False when both the variable are pointing to the same memory
# # location else True.
print(l1 is not l2)
print(l1 is not l3)
