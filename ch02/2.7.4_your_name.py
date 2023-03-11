#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    name = ''
    while name !=  'あなたの名前':
        print('あなたの名前を入力してください')
        name = input()
    print('どうも！')

if __name__ == '__main__':
    main()
