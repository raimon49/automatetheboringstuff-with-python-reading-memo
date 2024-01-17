#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from PIL import Image

    cat_im = Image.open('zophie.png')
    cat_copy_im = cat_im.copy()

    # 猫画像の顔部分矩形を指定して切り抜く（矩形タプルの左上の点は含まれるが右下の点は切り抜き領域に含まれない）
    face_im = cat_im.crop((335, 345, 565, 560))
    print(face_im.size) # (230, 215)

    cat_copy_im.paste(face_im, (0, 0))     # 左上の原点座標に貼り付け
    cat_copy_im.paste(face_im, (400, 500)) # X座標400, Y座標500に貼り付け
    cat_copy_im.save('pasted.png')         # 貼り付けた画像を別名称で保存

    cat_im_width, cat_im_height = cat_im.size
    face_im_width, face_im_height = face_im.size
    cat_copy_two = cat_im.copy()
    for left in range(0, cat_im_width, face_im_width):
        for top in range(0, cat_im_height, face_im_height):
            # 0 0
            # 0 215
            # 0 430
            # 0 645
            # 0 860
            # 0 1075
            # 230 0
            # 230 215
            # 230 430
            # 230 645
            # 230 860
            # 230 1075
            # 460 0
            # 460 215
            # 460 430
            # 460 645
            # 460 860
            # 460 1075
            # 690 0
            # 690 215
            # 690 430
            # 690 645
            # 690 860
            # 690 1075
            print(left, top)
            cat_copy_two.paste(face_im, (left, top))

    cat_copy_two.save('tiled.png')

if __name__ == '__main__':
    main()
