#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import openpyxl

    wb = openpyxl.load_workbook('produceSales.xlsx')
    print(type(wb))
    print(wb.sheetnames)

    sheet = wb['Sheet']
    print(type(sheet))

    a1 = sheet['A1']
    print(a1.value)
    b1 = sheet['B1']
    print(b1.value)

if __name__ == '__main__':
    main()

