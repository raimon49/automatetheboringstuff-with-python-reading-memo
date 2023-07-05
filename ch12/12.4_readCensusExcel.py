#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import openpyxl, pprint

    print('ワークブックを開いています...')
    wb = openpyxl.load_workbook('censuspopdata.xlsx')
    print(wb.sheetnames)
    sheet = wb['Population by Census Tract']
    country_data = {}

    print('行を読み込んでいます...')
    for row in range(2, sheet.max_row + 1):
        # スプレッドシートの1行に、ひとつの人口調査標準地域のデータがある
        state = sheet['B' + str(row)].value
        country = sheet['C' + str(row)].value
        pop = sheet['D' + str(row)].value

        # この州のキーが確実に存在するようにする
        country_data.setdefault(state, {})
        # この州のこの郡のキーが確実に存在するようにする
        country_data[state].setdefault(country, {'tracts': 0, 'pop': 0})
        # 各行が人口調査標準地域を表すので、数を1つ増やす
        country_data[state][country]['tracts'] += 1
        # この人口調査標準地域の人口だけ郡の人口を増やす
        country_data[state][country]['pop'] += int(pop)

    pprint.pprint(country_data)

if __name__ == '__main__':
    main()

