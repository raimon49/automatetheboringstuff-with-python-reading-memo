#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    """ピクニックの持ち物を出力する

    Args:
        items_dict: 道具の辞書データ
        left_width: 左余白の長さ
        right_width: 右余白の長さ

    Returns:
        None
    """
    def print_picnic(items_dict, left_width, right_width):
        print('PICNIC ITEMS'.center(left_width + right_width, '-'))
        for k, v in items_dict.items():
            print(k.ljust(left_width, '.') + str(v).rjust(right_width))

    picnic_items = {'sandwiches': 4,
                    'apples': 12,
                    'cupus': 4,
                    'cookies': 8000}
    print_picnic(picnic_items, 12, 5)
    print_picnic(picnic_items, 20, 6)

if __name__ == '__main__':
    main()

