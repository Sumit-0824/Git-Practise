# dictionary(dict):collection of key-value pairs separated by comma operator
# boundary : {}
# syntax: var_name = {key1:value1,key2:value2,...key n:value n}

d = {} #empty dict
print(type(d))
d1 = {'a':23,'b':56,(4,5):[1,2,3],'a':56}
print(d1)
print(len(d1))
# dict is ordered in nature
# Keys must be of immutable data type.
# dict is mutable datatype
# Values can be of any datatype.
# Key cannot be duplicated.
#Values can be accessed through keys only
# var_name[key]
print(d1['a'])

data = {'bangalore':25,'goa':35,'punjab':30}
print(data['bangalore'])
print(data['punjab'])
# print(data['pune'])  # error
data['punjab'] = 30
data['pune'] = 32
print(data)



data={'bangalore':25,'goa':35,'punjab':30}
print(data['bangalore'])               #25
print(data['goa'])                     #35
#print(data['pune'])       #error
data['goa'] =38             #It will be updated
data['pune'] =38         #It will be modify
print(data)           #{'bangalore': 25, 'goa': 38, 'punjab': 30, 'pune': 38}

print(dir(dict))




#-----------------------------------------------------------------------------
data={'bangalore':25,'goa':35,'punjab':30}
#Method in dictionary
#1.'get'
print(data.get('bangalore'))                  #25
print(data.get('25'))   # we cannot access with value#None
print(data.get('pune'))                        #None
print(data.get('pune','key is not found'))     #key is not found

#2.'update'
print(data.update({'goa':32,'mysore':27}))
print(data.update({'delhi':31}))
print(data)                                   #{'bangalore': 25, 'goa': 32, 'punjab': 30, 'mysore': 27, 'delhi': 31}




#3. items
print(data.items())                           #dict_items([('bangalore', 25), ('goa', 32), ('punjab', 30), ('mysore', 27), ('delhi', 31)])


#4.values
print(data.values())                          #dict_values([25, 32, 30, 27, 31])

#5.keys
print(data.keys())                            #dict_keys(['bangalore', 'goa', 'punjab', 'mysore', 'delhi'])


#Methods in dictionary--->get,update,items,keys,values