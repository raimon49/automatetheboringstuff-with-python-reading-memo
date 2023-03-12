#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    while True:
        print('あなたはJoe？')
        name = input()
        if name != 'Joe':
            continue
        print('こんにちはJoe、パスワードは？（魚）')
        password = input()
        if password == 'fish':
            break
    print('認証しました')

if __name__ == '__main__':
    main()
