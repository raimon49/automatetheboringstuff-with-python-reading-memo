#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import openpyxl

    wb = openpyxl.load_workbook('produceSales.xlsx')
    sheet = wb['Sheet']

if __name__ == '__main__':
    main()

