#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import cProfile, time, sys

    def calc_prod():
        product = 1
        for i in range(1, 10000):
            product = product * i

        return product

    sys.set_int_max_str_digits(50000) # require Python 3.11+
    start_time = time.time()
    prod = calc_prod()
    end_time = time.time()
    print('計算結果は{}桁です。'.format(len(str(prod))))
    print('計算時間は{}秒でした。'.format(end_time - start_time))

    # Pythonプロファイラを使った計測
    cProfile.runctx('calc_prod()', globals(), locals())


if __name__ == '__main__':
    main()
