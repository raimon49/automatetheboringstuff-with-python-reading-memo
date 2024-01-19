#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image

    cat_im = Image.open('zophie.png')
    width, height = cat_im.size

    quartersized_im = cat_im.resize((int(width / 2), int(height /2)))
    quartersized_im.save('quartersized.png')

if __name__ == '__main__':
    main()
