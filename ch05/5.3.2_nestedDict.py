#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    all_guests = {
        'アリス': {'リンゴ': 5, 'プレッツェル': 12},
        'ボブ': {'ハムサンド': 3, 'リンゴ': 2},
        'キャロル': {'コップ': 3, 'アップルパイ': 1},
    }

    def total_brought(guests, item):
        num_brought = 0
        for k, v in guests.items():
            num_brought = num_brought + v.get(item, 0)

        return num_brought

    print('持ち物の数')
    print('  -  リンゴ ' + str(total_brought(all_guests, 'リンゴ')))
    print('  -  コップ ' + str(total_brought(all_guests, 'コップ')))


if __name__ == '__main__':
    main()

