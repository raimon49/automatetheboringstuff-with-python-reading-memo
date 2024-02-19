#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image, ImageDraw

    im = Image.new('RGBA', (200, 200), 'white')
    draw = ImageDraw.Draw(im)

    draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')

if __name__ == '__main__':
    main()
