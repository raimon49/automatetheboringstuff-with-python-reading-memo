#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
import random

def main():
    secret_number = random.randint(1, 20)
    print('1から20までの数を当ててください。')

    # 最大6回聞く
    for guessess_taken in range(1, 7):
        print('数を入力してください。')
        guess = int(input())

        if guess < secret_number:
            print('小さいです。')
        elif guess > secret_number:
            print('大きいです。')
        else:
            # 当たったらforループを抜ける
            break

    if guess == secret_number:
        print('大当たり！' + str(guessess_taken) + '回で当たりました！')
    else:
        print('残念。正解は' + str(secret_number) + 'でした。')

if __name__ == '__main__':
    main()

