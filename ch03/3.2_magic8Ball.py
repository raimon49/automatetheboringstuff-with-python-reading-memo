#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
import random

def main():
    def get_answer(answer_number):
        if answer_number == 1:
            return '確かにそうだ'
        elif answer_number == 2:
            return '間違いなくそうだ'
        elif answer_number == 3:
            return 'はい'
        elif answer_number == 4:
            return 'なんとも。もういちどやってみて'
        elif answer_number == 5:
            return 'あとでもう一度聞いてみて'
        elif answer_number == 6:
            return '集中してもう一度聞いてみて'
        elif answer_number == 7:
            return '私の答えはノーです'
        elif answer_number == 8:
            return '見通しはそれほどよくない'
        else:
            return 'とても疑わしい'

    r = random.randint(1, 9)
    fortune = get_answer(r)
    print(fortune)

if __name__ == '__main__':
    main()

