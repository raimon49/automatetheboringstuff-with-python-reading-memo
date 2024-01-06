#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image

    im = Image.new('RGBA', (100, 200), 'purple')
    im.save('purpleImage.png')

    im2 = Image.new('RGBA', (20, 20))
    im2.save('transparentImage.png')


if __name__ == '__main__':
    main()
