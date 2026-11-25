import xlrd
path=r"C:\Users\Sumit\Desktop\job.xlsx"
xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter=True

workbook_obj=xlrd.open_workbook(path)
print(workbook_obj)
worksheet_obj=workbook_obj.sheet_by_name("data")
print(worksheet_obj)
rows=worksheet_obj.get_rows()
print(rows)
#1st Method
for row in rows:
    print(row)
#2nd method
for row in rows:
    print(row[0].value,row[1].value)

rows=worksheet_obj.get_rows()
header=next(rows)
print(header)


