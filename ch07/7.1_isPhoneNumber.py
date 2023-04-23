#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    def is_phone_number(text):
        if len(text) != 12:
            return False
        for i in range(0, 3):
            if not text[i].isdecimal():
                return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
        if text[i] != '-':
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True

    print('415-555-4141 は電話番号:')
    print(is_phone_number('415-555-4141'))
    print('Moshi Moshi は電話番号:')
    print(is_phone_number('Moshi Moshi'))

if __name__ == '__main__':
    main()

