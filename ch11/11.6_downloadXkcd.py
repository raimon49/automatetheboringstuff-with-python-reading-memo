#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import requests, os, bs4

    url = 'https://xkcd.com'
    os.makedirs('xkcd', exist_ok=True)

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('コミック画像が見つかりませんでした')
    else:
        print('コミック画像が見つかりました')
        comic_url = 'https:' + comic_elem[0].get('src')
        print('画像をダウンロード中 {}...'.format(comic_url))
        img = requests.get(comic_url)
        img.raise_for_status()

        with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as img_file:
            for chunk in img.iter_content(100000):
                img_file.write(chunk)

        prev_link = soup.select('a[rel="prev"]')[0]
        comic_url = 'https:' + prev_link.get('href')
        print(prev_link)


if __name__ == '__main__':
    main()

