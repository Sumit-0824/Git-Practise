import xlrd
path=r"C:\Users\Sumit\PycharmProjects\framework_selenium_M12\data\login.xlsx"
xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter=True

workbook_obj=xlrd.open_workbook(path)
#print(workbook_obj)
worksheet_obj=workbook_obj.sheet_by_name("login_cred")
#print(worksheet_obj)
rows=worksheet_obj.get_rows()
#print(rows)

for row in rows:
    print(row[0].value,row[1].value,row[2].value)

rows=worksheet_obj.get_rows()
header=next(rows)
#print(header)
d={row[0].value:(row[1].value,row[2].value) for row in rows}
print(d)

#output-{'txt_email': ('id', 'Email'), 'txt_pwd': ('name', 'Password'), 'btn_login': ('xpath', '(//input[@type="submit"])[2]')}