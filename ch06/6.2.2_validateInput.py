#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    while True:
        print('年齢を入力してください')
        age = input()
        if age.isdecimal():
            break
        print('年齢は数字で入力してください')

    while True:
        print('新しいパスワードを入力してください（英数字のみ）')
        password = input()
        if password.isalnum():
            break
        print('パスワードは英数字で入力してください')

if __name__ == '__main__':
    main()

