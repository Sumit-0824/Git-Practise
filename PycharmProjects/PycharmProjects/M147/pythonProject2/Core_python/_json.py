# JSON:javascript object notation
# json is a syntax for storing and exchanging the data
import csv
from json import *

# parse json :-converting json data to python data
# # by using json.loads() method

x =  '{ "name":"steve", "age":48, "city":"New York"}'
print(type(x))
x = loads(x)
print(x)
print(type(x))

# convert python data to json data
# by using the json.dumps() method
x = {
  "name": "steve",
  "age": 40,
  "city": "New York"
}
print(type(x))
x = dumps(x)
print(type(x))
'''
when you convert from python to json , python object are converted into the json equivalent:
python                  JSON
dict                    object
list                    Array
tuple                   Array
str                     String
int                     Number
float                   Number
True                    true
False                   false
None                    null
'''

x= {
    'name':'steve',
    'age': 40,
    'married':True,
    'divorced':False,
    'children':('anna','billy'),
    'pets':None,
    "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
        ]
}

x = dumps(x)


with open('file_handling/credit rating details.csv') as f:
    data = csv.DictReader(f)
    for line in data:
        j = line['Rating Details']
        print(type(j))
        decode = loads(j)
        print(type(decode))
        print(decode)
        break
