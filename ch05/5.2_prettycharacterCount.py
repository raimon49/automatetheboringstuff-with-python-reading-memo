#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
import pprint

def main():
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}

    for character in message:
        # if character in count:
        #     count[character] = 0
        # 上記のコードと同義
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    pprint.pprint(count)

    # 以下と同等
    print(pprint.pformat(count))

    # 登場回数順でソート
    pprint.pprint(sorted(count.items(), key=lambda x: x[1], reverse=True))

if __name__ == '__main__':
    main()

