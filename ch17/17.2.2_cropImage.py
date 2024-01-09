#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image

    cat_im = Image.open('zophie.png')

    # 猫画像の顔部分矩形を指定して切り抜く（矩形タプルの左上の点は含まれるが右下の点は切り抜き領域に含まれない）
    cropped_im = cat_im.crop((335, 345, 565, 560))
    # 新しい画像ファイルとして保存
    cropped_im.save('cropped.png')


if __name__ == '__main__':
    main()
