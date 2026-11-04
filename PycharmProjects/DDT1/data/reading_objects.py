import xlrd
path=r"C:\Users\Sumitkumar.Sinha\Desktop\selenium\login.xlsx"
xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter=True
def reading_locators():
    workbook_obj = xlrd.open_workbook(path)
    worksheet = workbook_obj.sheet_by_name('login_cred')
    rows = worksheet.get_rows()
    header = next(rows)
    return {row[0].value: (row[1].value, row[2].value) for row in rows}

#print(reading_locators())



