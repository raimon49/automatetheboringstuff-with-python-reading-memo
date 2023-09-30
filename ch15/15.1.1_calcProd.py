#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import time

    def calc_prod():
        product = 1
        for i in range(1, 10000):
            product = product * i

        return product

    start_time = time.time()
    prod = calc_prod()
    end_time = time.time()


if __name__ == '__main__':
    main()
