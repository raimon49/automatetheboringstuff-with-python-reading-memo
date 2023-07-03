#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import openpyxl, pprint

    print('ワークブックを開いています...')
    wb = openpyxl.load_workbook('censuspopdata.xlsx')
    print(wb.sheetnames)

if __name__ == '__main__':
    main()

