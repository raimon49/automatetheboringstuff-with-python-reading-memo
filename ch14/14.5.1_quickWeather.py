#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import json, requests, sys

    # コマンドラインから地名を組み立てる
    if len(sys.argv) < 2:
        print('Usage: quickWeather.py location')
        sys.exit()

    location = ' '.join(sys.argv[1:])
    location = '410020' # 佐賀県 伊万里
    url = 'https://weather.tsukumijima.net/api/forecast/city/{}'.format(
        location
    )
    response = requests.get(url)
    response.raise_for_status()


if __name__ == '__main__':
    main()
