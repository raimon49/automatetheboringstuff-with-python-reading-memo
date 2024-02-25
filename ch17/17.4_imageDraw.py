#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image, ImageDraw, ImageFont

    im = Image.new('RGBA', (200, 200), 'white')
    draw = ImageDraw.Draw(im)

    # 線分の描画
    draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
    # 矩形の描画
    draw.rectangle((20, 30, 60, 60), fill='blue')
    # 楕円の描画
    draw.ellipse((120, 30, 160, 60), fill='red')
    # 5点から構成される多角形の描画
    draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
    for i in range(100, 200, 10):
        # 線のパターンを描画
        draw.line([(i, 0), (200, i - 100)], fill='green')

    im.save('drawing.png')

    im = Image.new('RGBA', (200, 200), 'white')
    draw = ImageDraw.Draw(im)
    arial_font = ImageFont.truetype('DejaVuSansMono.ttf', 32)

if __name__ == '__main__':
    main()
