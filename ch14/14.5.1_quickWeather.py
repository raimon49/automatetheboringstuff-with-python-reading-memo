#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import json, requests, sys

    # コマンドラインから地名を組み立てる
    if len(sys.argv) < 2:
        print('Usage: quickWeather.py location')
        sys.exit()

    # 天気予報 API（livedoor 天気互換）からデータ取得
    # See: https://weather.tsukumijima.net/
    # ※原著ではOpenWeatherMap API (openweathermap.org) を利用している
    location = ' '.join(sys.argv[1:])
    location = '410020' # 佐賀県 伊万里
    url = 'https://weather.tsukumijima.net/api/forecast/city/{}'.format(
        location
    )
    response = requests.get(url)
    response.raise_for_status()

    weather_data = json.loads(response.text)
    w = weather_data['forecasts']
    day0 = w[0]
    day1 = w[1]
    day2 = w[2]

    print('今日の{}: '.format(weather_data['title']))
    print(day0['telop'], '-', day0['detail']['weather'])
    print('明日: ')
    print(day1['telop'], '-', day1['detail']['weather'])
    print('明後日: ')
    print(day2['telop'], '-', day2['detail']['weather'])


if __name__ == '__main__':
    main()
