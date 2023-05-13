#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import zipfile, os
    example_zip = zipfile.ZipFile('example.zip')
    print(example_zip.namelist())

    spam_info = example_zip.getinfo('spam.txt')
    print('spam.txt: filesize: ' + str(spam_info.file_size))
    print('spam.txt: compress_size: ' + str(spam_info.compress_size))
    size_raito = round(spam_info.file_size / spam_info.compress_size, 2)
    print('圧縮ファイルは{}倍小さい!'.format(size_raito))

if __name__ == '__main__':
    main()

