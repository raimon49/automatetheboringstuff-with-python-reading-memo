#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image

    cat_im = Image.open('zophie.png')
    width, height = cat_im.size

    quartersized_im = cat_im.resize((int(width / 2), int(height /2))) # 半分の大きさにリサイズ
    quartersized_im.save('quartersized.png')
    svelte_im = cat_im.resize((width, height + 300))                  # 縦長の画像にリサイズ
    svelte_im.save('svelte.png')

    thumb_im = cat_im.copy()
    print(thumb_im.size) # (816, 1088)
    thumb_im.thumbnail((100, 100))
    print(thumb_im.size) # (75, 100)
    thumb_im.save('thumbnail.jpg')

if __name__ == '__main__':
    main()
