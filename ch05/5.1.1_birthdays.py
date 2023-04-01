#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    birthdays = {
        'アリス': '4/1',
        'ボブ': '12/12',
        'キャロル': '4/4',
    }

    while True:
        print('名前を入力してください（終了するにはEnterだけ押してください）')
        name = input()
        if name == '':
            break

        if name in birthdays: # 変数birthdaysにnameが辞書キーとして登録されているか
            print(name + 'の誕生日は' + birthdays[name])
        else:
            print(name + 'の誕生日は未登録です。')
            print('誕生日を入力してください')
            bday = input()
            birthdays[name] = bday # キー・バリュー・ペアとして追加登録
            print('誕生日データベースを更新しました。')

if __name__ == '__main__':
    main()

