#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import requests, os, bs4, threading

    url = 'https://xkcd.com'
    os.makedirs('xkcd', exist_ok=True)

    def download_xkcd(start_comic, end_comic):
        for url_number in range(start_comic, end_comic):
            # ページをダウンロードする
            print('ページをダウンロード中 {}/{}'.format(url, url_number))
            res = requests.get('{}/{}'.format(url, url_number))
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')

            # コミックの画像URLを見つける
            comic_elem = soup.select('#comic img')
            if comic_elem == []:
                print('コミック画像が見つかりませんでした')
            else:
                print('コミック画像が見つかりました')
                comic_url = 'https:' + comic_elem[0].get('src')

                # 画像をダウンロードする
                print('画像をダウンロード中 {}...'.format(comic_url))
                img = requests.get(url)
                img.raise_for_status()
                # 画像を./xkcd ディレクトリに保存する
                with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as img_file:
                    for chunk in img.iter_content(100000):
                        img_file.write(chunk)

    # Treadオブジェクトを生成して開始する
    download_threads = []
    for i in rainge(1, 1400, 100):
        download_thread = threading.Thread(target=download_xkcd, args=(i, i + 100))
        download_threads.append(download_thread)
        download_thread.start()

    # TODO: すべてのスレッドが終了するのを待つ
    for download_thread in download_threads:
        download_thread.join()


if __name__ == '__main__':
    main()

