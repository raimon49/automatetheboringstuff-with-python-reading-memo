#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
import sys

def main():
    print('終了するにはexitと入力してください')
    while True:
        response = input()
        if response == 'exit':
            sys.exit()
        print(response + 'と入力されました')

if __name__ == '__main__':
    main()

