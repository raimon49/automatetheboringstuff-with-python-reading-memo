#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import logging
    logging.basicConfig(level=logging.DEBUG,
                        format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.debug('プログラム開始')

    def factorial(n):
        logging.debug('factorial({})開始'.format(n))
        total = 1
        for i in range(n + 1):
            total *= i
            logging.debug('i = {}, total = {}'.format(i, total))

        logging.debug('factorial({})終了'.format(n))

        return total

    print(factorial(5))
    logging.debug('プログラム終了')

if __name__ == '__main__':
    main()

