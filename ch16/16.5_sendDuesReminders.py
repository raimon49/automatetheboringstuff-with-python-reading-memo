#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import openpyxl, smtplib, sys

    wb = openpyxl.load_workbook('duesRecords.xlsx')
    sheet = wb['Sheet1']

    last_col = sheet.max_column
    last_month = sheet.cell(row=1, column=last_col).value # 最新月を取得

    # TODO: 会員の支払い状況を調べる
    unpaied_members = {}
    for r in range(2, sheet.max_row + 1):
        payment = sheet.cell(row=r, column=last_col).value # 'paid' or None
        if payment != 'paid':
            # 支払い済みでない会員の情報を取得
            name = sheet.cell(row=r, column=1).value
            email = sheet.cell(row=r, column=2).value
            unpaied_members[name] = email
    # TODO: メールアカウントにログインする
    # TODO: リマインダーメールを送信する


if __name__ == '__main__':
    main()
