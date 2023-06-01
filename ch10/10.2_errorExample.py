#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    def spam():
        bacon()

    def bacon():
        raise Exception('これはエラーメッセージです。')

    import traceback
    try:
        spam()
    except:
        error_file = open('errorInfo.txt', 'w')
        error_file.write(traceback.format_exc())
        error_file.close()
        print('トレースバック情報をerrorInfo.txtに書き出しました')

if __name__ == '__main__':
    main()

