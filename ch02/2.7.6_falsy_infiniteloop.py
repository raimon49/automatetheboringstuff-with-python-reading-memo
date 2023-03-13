#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    name = ''
    # 変数nameが空文字の間はループ
    while not name:
        print('名前を入力してください')
        name = input()
        print('同伴者は何人ですか？')
        num_of_guests = int(input())
        # 変数num_of_guestsが1以上の時に出力
        if num_of_guests:
            print('同伴者用の場所があるか確認してください')
        print('受け付けました')

if __name__ == '__main__':
    main()
