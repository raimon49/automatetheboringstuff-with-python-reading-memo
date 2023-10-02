#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import time

    for i in range(3):
        print('Tick')
        time.sleep(1)
        print('Tock')
        time.sleep(1)


if __name__ == '__main__':
    main()
