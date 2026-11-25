import xlrd
path=r"C:\Users\Sumit\PycharmProjects\Shopperstacx application\data\loginshopper.xlsx"
xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter=True
def reading_locators():
    workbook_obj = xlrd.open_workbook(path)
    worksheet_obj = workbook_obj.sheet_by_name("login_cred")
    #rows = worksheet_obj.get_rows()
    # for row in rows:
    #     print(row[0].value, row[1].value, row[2].value)

    rows = worksheet_obj.get_rows()
    header = next(rows)
    return {row[0].value: (row[1].value, row[2].value) for row in rows}
#print(reading_locators())
#output-{'txt_email': ('id', 'Email'), 'txt_pwd': ('name', 'Password'), 'btn_login': ('xpath', '(//input[@type="submit"])[2]')}