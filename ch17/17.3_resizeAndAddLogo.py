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

    # TODO: 画像をサイズ変更する

    # TODO: ロゴを追加する

    # TODO: 変更を保存する

if __name__ == '__main__':
    main()
