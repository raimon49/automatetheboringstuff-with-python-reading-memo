#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image, ImageDraw

    im = Image.new('RGBA', (200, 200), 'white')
    draw = ImageDraw.Draw(im)

    draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
    draw.rectangle((20, 30, 60, 60), fill='blue')
    draw.ellipse((120, 30, 160, 60), fill='red')
    draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')

if __name__ == '__main__':
    main()
