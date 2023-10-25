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

    halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
    newyear2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
    oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
    print(halloween2015 == oct31_2015) # True
    print(halloween2015 > newyear2016) # False
    print(newyear2016 > halloween2015) # True
    print(newyear2016 != oct31_2015)   # True

    delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
    print(delta.days, delta.seconds, delta.microseconds) # 11 36548 0
    print(delta.total_seconds())                         # 986948.0
    print(str(delta))                                    # 11 days, 10:09:08

    dt_now = datetime.datetime.now()
    print(dt_now)
    thousand_days = datetime.timedelta(days=1000)
    print(dt_now + thousand_days) # 現在日時の1,000日後を計算

    oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
    about_thirty_years = datetime.timedelta(days=365 * 30) # 1年365日と仮定して30年の期間を生成
    print(oct21st)                              # 2015-10-21 16:29:00
    print(oct21st - about_thirty_years)         # 1985-10-28 16:29:00
    print(oct21st  -  (2 * about_thirty_years)) # 1955-11-05 16:29:00

    print(oct21st.strftime('%Y/%m/%d %H:%M:%S')) # 2015/10/21 16:29:00
    print(oct21st.strftime('%I:%M: %p'))         # 04:29: PM
    print(oct21st.strftime("%B of '%y"))         # October of '15

    print(datetime.datetime.strptime(
        'October 21, 2015', '%B %d, %Y'            # 2015-10-21 00:00:00
    ))
    print(datetime.datetime.strptime(
        '2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S' # 2015-10-21 16:29:00
    ))
    print(datetime.datetime.strptime(
        "October of '15", "%B of '%y"              # 2015-10-01 00:00:00
    ))
    print(datetime.datetime.strptime(
        "November of '63", "%B of '%y"
    ))

if __name__ == '__main__':
    main()
