#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
import random

def main():
    def spam(divide_by):
        try:
            return 42 / divide_by
        except ZeroDivisionError:
            print('エラー: 不正な引数です', end='')
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))


if __name__ == '__main__':
    main()

