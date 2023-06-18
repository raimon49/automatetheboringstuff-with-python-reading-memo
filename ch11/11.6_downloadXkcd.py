#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import requests, os, bs4

    res = requests.get('https://xkcd.com')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('コミック画像が見つかりませんでした')
    else:
        print('コミック画像が見つかりました')
        comic_url = 'https:' + comic_elem[0].get('src')
        print(comic_url)


if __name__ == '__main__':
    main()

