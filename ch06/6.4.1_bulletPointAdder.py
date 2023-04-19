#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    text = """日本の野鳥一覧
犬の品種一覧
猫の品種一覧
家畜一覧"""

    lines = text.split('\n')
    for i in range(len(lines)):
        print('* ' + lines[i])

if __name__ == '__main__':
    main()

