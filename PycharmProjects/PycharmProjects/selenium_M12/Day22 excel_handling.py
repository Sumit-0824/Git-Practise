"""
xlrd
pip install xlrd==1.2.0
pip list

"""
#Known as data driven testing
import xlrd

path=r"C:\Users\Sumit\Desktop\job.xlsx"
xlrd.xlsx.ensure_elementtree_imported(False,None)   #2 keyword False and None
xlrd.xlsx.Element_has_iter= True

workbook_obj=xlrd.open_workbook(path)
print(workbook_obj)     #<xlrd.book.Book object at 0x00000241D485B090>  #Return type book object

worksheet_obj=workbook_obj.sheet_by_name("data")
print(worksheet_obj)    #<xlrd.sheet.Sheet object at 0x0000014A91A156D0>  #Return type Sheet object

rows=worksheet_obj.get_rows()
print(rows)            #<generator object Sheet.get_rows.<locals>.<genexpr> at 0x000001A1A54857E0> #generator return yield
#1st method
for row in rows:
    print(row)
#2nd method
for row in rows:
    print(row[0].value,row[1].value)
'''
#output-in the form of list
[text:'Name', text:'Profession']
[text:'John', text:'Doctor']
[text:'steve', text:'Engineer']
[text:'max', text:'Trainee']

'''

rows=worksheet_obj.get_rows()
header=next(rows)         #Skipping header-1st row
print(header)

#[text:'Name', text:'Profession']

#Read as dictionary    #Comprehension
d={row[0].value:row[1].value for row in rows}
print(d)

#{'John': 'Doctor', 'steve': 'Engineer', 'max': 'Trainee'}
