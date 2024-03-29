#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image

    # 幅100x高さ100で紫の背景色を持つ画像を生成
    im = Image.new('RGBA', (100, 200), 'purple')
    im.save('purpleImage.png')

    # 幅20x高さ20で紫の背景色を持たない画像を生成
    im2 = Image.new('RGBA', (20, 20))
    im2.save('transparentImage.png')


if __name__ == '__main__':
    main()
