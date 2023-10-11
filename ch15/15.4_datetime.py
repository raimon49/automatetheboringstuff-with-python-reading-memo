#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import datetime

    print(datetime.datetime.now())

    dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
    print(dt.year, dt.month, dt.day)
    print(dt.hour, dt.minute, dt.second)

if __name__ == '__main__':
    main()
