#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image

    cat_im = Image.open('zophie.png')
    cropped_im = cat_im.crop((335, 345, 565, 560))


if __name__ == '__main__':
    main()
