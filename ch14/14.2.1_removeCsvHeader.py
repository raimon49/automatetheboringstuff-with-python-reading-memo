#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import csv, os

    os.makedirs('headerRemoved', exist_ok=True)

    # カレントディレクトリの全ファイルをループ
    for csv_filename in os.listdir('.'):
        if not csv_filename.endswith('.csv'):
            # CSVファイルでなければスキップ
            continue

        print('見出し削除中' + csv_filename + '...')

        # TODO: CSVファイルを読み込む（最初の行をスキップする）
        csv_rows = []
        with open(csv_filename) as csv_file_obj:
            reader_obj = csv.reader(csv_file_obj)
            for row in reader_obj:
                if reader_obj.line_num == 1:
                    continue

            csv_rows.append(row)

        # TODO: CSVファイルを書き出す

if __name__ == '__main__':
    main()
