#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import os
    from PIL import Image

    SQUARE_FIT_SIZE = 300
    LOGO_FILENAME = 'catlogo.png'

    logo_im = Image.open(LOGO_FILENAME)
    logo_width, logo_height = logo_im.size

    # TODO: カレントディレクトリの全画像をループする
    os.makedirs('whithLogo', exist_ok=True)

    for filename in os.listdir('.'):
        # 画像以外のファイル・ロゴファイルはスキップ
        if not (filename.endswith('.png') or filename.endswith('.jpg')) \
                or filename == LOGO_FILENAME:
            continue

        im = Image.open(filename).copy()

        # TODO: 画像をサイズ変更する
        im.thumbnail((SQUARE_FIT_SIZE, SQUARE_FIT_SIZE))
        width, height = im.size

        # TODO: ロゴを追加する
        print('ロゴを追加中 {}...'.format(filename))
        im.paste(logo_im,
                 (width - logo_width, height - logo_height),
                 logo_im)

        # TODO: 変更を保存する
        im.save(os.path.join('withLogo', filename))

if __name__ == '__main__':
    main()
