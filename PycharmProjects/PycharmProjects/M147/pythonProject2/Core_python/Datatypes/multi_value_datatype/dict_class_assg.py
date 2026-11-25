d = {'a':'apple','b':[1,2,3,4,5,6],'c':{"d":'dog','p':12}}
#pple
print(d['a'][1::])
#[1,2,3,4,5,6]
print(d['b'])
#[1,3,5]
print(d['b'][::2])
#[2,4,6]
print(d['b'][1:6:2])
#[6,5,4,3,2,1]
print(d['b'][::-1])
#'og'
print(d['c']['d'][1::])
#'god'
print(d['c']['d'][::-1])
#elppa
print(d['a'][::-1])


# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])                    #hello
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])                      #hello
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])       #hello