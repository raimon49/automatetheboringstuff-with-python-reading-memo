#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import shutil, os, re

    # 米国式日付(MM-DD-YYYY)のファイル名にマッチする正規表現を作る
    date_pattern = re.compile(r"""^(.*?)          # 日付の前の全テキスト
                                  ((0|1)?\d)-     # 月を表す1,2桁の数字
                                  ((0|1|2|3)?\d)- # 日を表す1,2桁の数字
                                  ((19|20)\d\d)   # 年を表す4桁の数字
                                  (.*?)$          # 日付の後の全テキスト
                              """, re.VERBOSE)
    # カレントディレクトリの全ファイルをループする
    for amer_filename in os.listdir('.'):
        mo = date_pattern.search(amer_filename)

        # 日付のないファイルをスキップする
        if mo == None:
            continue

        # ファイル名を部分分解する
        before_part = mo.group(1)
        month_part = mo.group(2)
        day_part = mo.group(4)
        year_part = mo.group(6)
        after_part = mo.group(8)
        # 欧州式の日付ファイルを作る
        euro_filename = before_part + day_part + '-' + month_part + '-' + \
                        year_part + after_part
        print('Renaming "{}" to "{}"...'.format(
            amer_filename,
            euro_filename
        ))
        # ファイル名を変更する
        # (git reset --hard HEADで戻す)
        shutil.move(amer_filename, euro_filename)


if __name__ == '__main__':
    main()

