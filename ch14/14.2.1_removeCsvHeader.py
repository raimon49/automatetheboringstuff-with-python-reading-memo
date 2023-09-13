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

        # TODO: CSVファイルを書き出す

if __name__ == '__main__':
    main()
