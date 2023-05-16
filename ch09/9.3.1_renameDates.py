#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import shutil, os, re

    # 米国式日付(MM-DD-YYYY)のファイル名にマッチする正規表現を作る
    date_pattern = re.compile(r"""^(.*?)          # 月を表す1,2桁の数字
                                  ((0|1)?\d)-     # 日を表す1,2桁の数字
                                  ((0|1|2|3)?\d)- # 年を表す4桁の数字
                                  ((19|20)\d\d)   # 日付の後の全テキスト
                                  (.*?)$
                              """, re.VERBOSE)
    # TODO: カレントディレクトリの全ファイルをループする
    # TODO: 日付のないファイルをスキップする
    # TODO: ファイル名を部分分解する
    # TODO: 欧州式の日付ファイルを作る
    # TODO: ファイル名を変更する


if __name__ == '__main__':
    main()

