#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import datetime, time

    print(datetime.datetime.now())

    dt = datetime.datetime(2015, 10, 21, 16, 29, 0) # 2023-10-11 21:06:01.092813
    print(dt.year, dt.month, dt.day)                # 2015 10 21
    print(dt.hour, dt.minute, dt.second)            # 15 29 0

    print(datetime.datetime.fromtimestamp(10000000))    # 1970-04-27 02:46:40
    print(datetime.datetime.fromtimestamp(time.time())) # 現在時刻から日付・時刻を生成

if __name__ == '__main__':
    main()
