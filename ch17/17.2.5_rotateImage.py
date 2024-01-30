#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image

    cat_im = Image.open('zophie.png')

    cat_im.rotate(90).save('rotated90.png')   # 反時計回りに90度回転
    cat_im.rotate(180).save('rotated180.png') # 上下反転
    cat_im.rotate(270).save('rotated270.png') # 反時計回りに270度回転

    cat_im.rotate(6).save('rotated6.png')                       # 回転で見切れた部分は切り取られる
    cat_im.rotate(6, expand=True).save('rotated6_expanded.png') # 回転部分が画像内に収まるよう拡大

    cat_im.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')

if __name__ == '__main__':
    main()
