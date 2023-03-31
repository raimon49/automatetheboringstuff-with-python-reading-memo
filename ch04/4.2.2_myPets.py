#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    my_pets = ['Zophie', 'Pooka', 'Fat-tail']
    print('ペットの名前を入力してください')
    name = input()
    if name not in my_pets:
        print(name + 'という名前のペットは飼っていません')
    else:
        print(name + 'は私のペットです')

if __name__ == '__main__':
    main()

