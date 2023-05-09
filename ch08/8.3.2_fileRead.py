#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    sonnet_file = open('sonnet29.txt')
    lines = sonnet_file.readlines()

    print(lines) # 各行の末尾には改行文字\nが付いている
    print()
    print('\n'.join(lines))

if __name__ == '__main__':
    main()

