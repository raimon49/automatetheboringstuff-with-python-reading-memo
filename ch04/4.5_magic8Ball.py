#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
import random

def main():
    messages = [
        '確かにそうだ',
        '間違いなくそうだ',
        'はい',
        'なんとも。もういちどやってみて',
        'あとでもう一度聞いてみて',
        '集中してもう一度聞いてみて',
        '私の答えはノーです',
        '見通しはそれほどよくない',
        'とても疑わしい',
    ]
    # 3.2のmagic8Ball.pyと同じ動作をする
    print(messages[random.randint(0, len(messages) - 1)])

if __name__ == '__main__':
    main()

