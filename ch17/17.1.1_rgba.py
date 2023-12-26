#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import ImageColor

    print(ImageColor.getcolor('red', 'RGBA'))


if __name__ == '__main__':
    main()
