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

        # 見出し処理中のファイル名を出力
        print('見出し削除中' + csv_filename + '...')

        # CSVファイルを読み込む（最初の行をスキップする）
        csv_rows = []
        with open(csv_filename) as csv_file_obj:
            reader_obj = csv.reader(csv_file_obj)
            for row in reader_obj:
                if reader_obj.line_num == 1:
                    # 最初の行をスキップする
                    continue

                # 2行目以降を追加
                csv_rows.append(row)

        # CSVファイルを書き出す
        with open(os.path.join('headerRemoved', csv_filename), 'w', newline='') as csv_file_obj:
            csv_writer = csv.writer(csv_file_obj)
            for row in csv_rows:
                csv_writer.writerow(row)

if __name__ == '__main__':
    main()
