import xlrd


def read_xls(file_name):
    xls_file = xlrd.open_workbook(file_name)
    print("The number of worksheets is {}".format(xls_file.nsheets))
    print("Worksheet name(s): {}".format(xls_file.sheet_names()))

    sheet = xls_file.sheet_by_index(0)
    print("{}: row={}, col={}".format(sheet.name, sheet.nrows, sheet.ncols))
    print("Cell 11 is {}".format(sheet.cell_value(rowx=1, colx=1)))

    for i in range(1, sheet.nrows):
        # print(sheet.row(rx))
        print("{}:\t{}".format(sheet.cell_value(rowx=i, colx=0), sheet.cell_value(rowx=i, colx=1)))


read_xls("Book1.xls")
