#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import openpyxl

    wb = openpyxl.load_workbook('produceSales.xlsx')
    sheet = wb['Sheet']

    # 農産物の種類と、更新する価格
    PRICE_UPDATES = {'Garlic': 3.07,
                     'Celery': 1.19,
                     'Lemon': 1.27}

    # 行をループして価格を更新する
    for row_num in range(2, sheet.max_row + 1): # 先頭行は表見出しのためスキップ
        produce_name = sheet.cell(row = row_num, column=1).value
        if produce_name in PRICE_UPDATES:
            sheet.cell(row=row_num, column=2).value = PRICE_UPDATES[produce_name]

    # 間違った内容で更新されないよう、元のファイルを上書きせず別名で保存
    wb.save('updatedProduceSales.xlsx')

if __name__ == '__main__':
    main()

