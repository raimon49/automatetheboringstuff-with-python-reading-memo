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
        if text[7] != '-':
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True

    def is_phone_number_with_regex(text):
        import re
        phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        mo = phone_num_regex.search(text)

        return mo != None

    print('415-555-4141 は電話番号:')
    print(is_phone_number('415-555-4141'))
    print('Moshi Moshi は電話番号:')
    print(is_phone_number('Moshi Moshi'))

    message = '明日415-555-1011に電話してください。オフィスは415-555-9999です。'
    for i in range(len(message)):
        chunk = message[i:i+12]
        if is_phone_number(chunk):
            print('電話番号が見つかりました: ' + chunk)
    print('完了')

if __name__ == '__main__':
    main()

