#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image

    im = Image.new('RGBA', (100, 100))
    print(im.getpixel((0, 0))) # (0, 0, 0, 0)

if __name__ == '__main__':
    main()
