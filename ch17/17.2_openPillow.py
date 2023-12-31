#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image

    cat_im = Image.open('zophie.png')
    print(cat_im) # <PIL.PngImagePlugin.PngImageFile image mode=RGB size=816x1088 at 0x7F130DE79E50>


if __name__ == '__main__':
    main()
