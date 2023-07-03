#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import openpyxl, pprint

    print('ワークブックを開いています...')
    wb = openpyxl.load_workbook('censuspopdata.xlsx')
    print(wb.sheetnames)
    sheet = wb['Population by Census Tract']
    country_cata = {}

    print('行を読み込んでいます...')
    for row in range(2, sheet.max_row + 1):
        state = sheet['B' + str(row)].value
        country = sheet['C' + str(row)].value
        pop = sheet['D' + str(row)].value

if __name__ == '__main__':
    main()

