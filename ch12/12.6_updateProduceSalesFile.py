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

    # TODO: 行をループして価格を更新する

if __name__ == '__main__':
    main()

