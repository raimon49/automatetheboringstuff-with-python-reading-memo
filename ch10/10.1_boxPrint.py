#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    def box_print(symbol, width, height):
        if len(symbol) != 1:
            raise Exception('symbolは1文字の文字列でなければならない')
        if width <= 2:
            raise Exception('widthは2より大きくなければならない')
        if height <= 2:
            raise Exception('heightは2より大きくなければならない')

        print(symbol * width)

if __name__ == '__main__':
    main()

