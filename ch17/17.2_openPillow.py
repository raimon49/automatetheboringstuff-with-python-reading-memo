#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image

    cat_im = Image.open('zophie.png')
    print(cat_im) # <PIL.PngImagePlugin.PngImageFile image mode=RGB size=816x1088 at 0x7F130DE79E50>

    print(cat_im.size) # (816, 1088)

    width, height = cat_im.size
    print(width)  # 816
    print(height) # 1088

    print(cat_im.filename) # zophie.png

    print(cat_im.format) # PNG

    print(cat_im.format_description) # Portable network graphics

    # JPEGフォーマットで保存
    # cat_im.save('zophie.jpg')


if __name__ == '__main__':
    main()
