#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import ImageColor

    print(ImageColor.getcolor('red', 'RGBA'))            # (255, 0, 0, 255)
    print(ImageColor.getcolor('RED', 'RGBA'))            # (255, 0, 0, 255)
    print(ImageColor.getcolor('Black', 'RGBA'))          # (0, 0, 0, 255)
    print(ImageColor.getcolor('chocolate', 'RGBA'))      # (210, 105, 30, 255)
    print(ImageColor.getcolor('CornflowerBlue', 'RGBA')) # (100, 149, 237, 255)


if __name__ == '__main__':
    main()
