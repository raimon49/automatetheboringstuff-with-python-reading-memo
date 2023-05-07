#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import re
    phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

    # 複雑な正規表現を三重引用符テキストでコメント付きで管理する
    phone_num_complex_regex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?           # 3桁の市外局番で()が付いてもよい
        (\s|-|\.)?                   # 区切り（スペース or ハイフン or ドット）
        \d{3}                        # 3桁の市内局番
        (\s|-|\.)                    # 区切り（スペース or ハイフン or ドット）
        \d{4}                        # 4桁の番号
        (\s*(ext|x|ext.)\s*\d{2,5})? # 2～5桁の内線番号
    )''', re.VERBOSE | re.IGNORECASE | re.DOTALL)

    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+  # ユーザー名
        @                  # @ 記号
        [a-zA-Z0-9.-] +    # ドメイン名
        (\.[a-zA-Z]{2,4})  # ドットなんとか
    )''', re.VERBOSE)

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
        mo = phone_num_regex.search(text)

        return mo != None

    def is_phone_number_with_complex_regex(text):
        mo = phone_num_complex_regex.search(text)

        return mo != None

    def is_email_with_regex(text):
        mo = email_regex.search(text)

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

    number = '123-456-789'
    assert is_phone_number(number) == is_phone_number_with_regex(number)

    falsy_number = '12-3456-789'
    assert is_phone_number(falsy_number) == is_phone_number_with_regex(falsy_number)

    assert is_phone_number_with_complex_regex('(012)-333-4444')
    assert is_phone_number_with_complex_regex('012.333.4444')
    assert is_phone_number_with_complex_regex('012 333 4444')
    assert not is_phone_number_with_complex_regex('0123334444')

    assert is_email_with_regex('taro-hanako1234@example.com')
    assert not is_email_with_regex('$@example.com')

if __name__ == '__main__':
    main()

