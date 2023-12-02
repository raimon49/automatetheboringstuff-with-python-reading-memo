#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import openpyxl, smtplib, sys

    wb = openpyxl.load_workbook('duesRecords.xlsx')
    sheet = wb['Sheet1']

    last_col = sheet.max_column
    last_month = sheet.cell(row=1, column=last_col).value # 最新月を取得


if __name__ == '__main__':
    main()
