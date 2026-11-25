# csv:(comma seperated values):is simple file formate used to store tabular data
# such as spreadsheet or database.
# - for working CSV files in python ,there is a in-built module called csv
import csv
# WRITING CSV FILE:
# There are2 two ways:
# 1. csv.writer(file) --> [] --> wirterow -->['','',''], witerrows-->[['',''],['',''],['','']]
# 2. csv.DictWriter(file) --> {} --> wirterow -->{'','',''} , witerrows-->[{'',''},{'',''},{'',''}]

with open('company.csv','w',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['name','share','price'])
    csv_writer.writerow(['IBM',98,88])
    csv_writer.writerows([['google',89,99],['yahoo',87,87]])

with open('sample.csv','w',newline='') as f1:
    csv_writer = csv.DictWriter(f1,['name','shares','price'])
    csv_writer.writeheader()
    csv_writer.writerow({'name':'IBM','shares':98,'price':79})
    csv_writer.writerows([{'name':'google','shares':77,'price':99},{'name':'yahoo','shares':99,'price':78}])

# READING CSV FILE:
# there are 2 ways:
# 1. csv.reader(file)
# note:iterator object which holds each data record in the form of python list
# 2. csv.DictReader(file)
# note:iterator object which holds each data record in the form of python dict

with open(r'C:\Users\Sumit\Desktop\Qspider python classes\Files\employees2.csv','r') as f_csv:
    rows = csv.reader(f_csv)
    for row in rows:
        print(row)

with open(r'C:\Users\Sumit\Desktop\Qspider python classes\Files\employees2.csv','r') as f_csv:
    rows = csv.DictReader(f_csv)
    for row in rows:
        print(row)

def readcsv():
    records = []
    with open(r'C:\Users\Sumit\Desktop\Qspider python classes\Files\employees2.csv', 'r') as f_csv:
        rows = csv.reader(f_csv)
        rows.__next__() # remove the header
        expecting_types = [str,str,int,str,str]
        for row in rows:
            converted = [ex_ty(item) for ex_ty,item in zip(expecting_types,row) ]
            records.append(converted)
    return records

print(readcsv())

# what is the total amount that paying to all employees as salary?
def total_pay():
    data = readcsv()
    return sum([item[2] for item in data])

print(total_pay())
#output-37400
# how many number of `male` and `female` employees are working in the company?
from  collections import Counter
def gender():
    data = readcsv()
    return Counter([item[3] for item in data])
print(gender())
#Output-Counter({'male': 7, 'female': 3})
def _gender():
    data = readcsv()
    res = [item[3] for item in data]
    return {i:res.count(i) for i in res}
print(_gender())
#{'male': 7, 'female': 3}
# who is the highest paid employee?
def highest_pay():
    data = readcsv()
    return sorted(data,key = lambda i:i[2])[-1]
print(highest_pay())
#output-['guido', 'rossum', 8000, 'male', 'development']
# i want to know who all are taking more than $3000?
def morethan_3k():
    data = readcsv()
    return [i for i in data if i[2]>3000]
    #return len([i for i in data if i[2]>3000]) =FOr total count more than 3000
print(morethan_3k())
#Output-[['steve', 'jobs', 4000, 'male', 'development'], ['john', 'doe', 3500, 'male', 'testing'], ['steve', 'wozniak', 4500, 'male', 'marketing'], ['tim', 'cook', 6000, 'male', 'marketing'], ['guido', 'rossum', 8000, 'male', 'development'], ['johny', 'ive', 4900, 'male', 'development']]
# i want to know how many unique teams are present?
def unique_team():
    data=readcsv()
    return {i[-1] for i in data}
print(unique_team())
#Output-{'marketing', 'testing', 'development'}
# how many member present in each team

def m_team():
    data=readcsv()
    res=[i[-1]for i in data]

    return {i:res.count(i)for i in res}
print(m_team())

#Output-{'development': 4, 'testing': 3, 'marketing': 3}