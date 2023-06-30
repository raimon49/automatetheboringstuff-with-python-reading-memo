#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import openpyxl
    from openpyxl.utils import get_column_letter, column_index_from_string

    wb = openpyxl.load_workbook('produceSales.xlsx')
    print(type(wb))
    print(wb.sheetnames)

    sheet = wb['Sheet']
    print(type(sheet))

    a1 = sheet['A1']
    print(a1.value)
    b1 = sheet['B1']
    print(b1.value)

    for i in range(1, 8, 2):
        print(i, sheet.cell(row=i, column=2).value)

    print(sheet.max_row)
    print(sheet.max_column)

    print(get_column_letter(1))
    print(get_column_letter(2))

if __name__ == '__main__':
    main()

