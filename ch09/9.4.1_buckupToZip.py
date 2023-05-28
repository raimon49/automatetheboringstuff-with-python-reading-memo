#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import zipfile, os

    def backup_to_zip(folder):
        # フォルダ全体をZIPファイルにバックアップする
        folder = os.path.abspath(folder)

        number = 1
        while True:
            zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
            # 「対象フォルダ名_連番」の圧縮ファイル名を決める
            if not os.path.exists(zip_filename):
                break

            number = number + 1

        # TODO:  ZIPファイルを作成する
        print('Creating {}...'.format(zip_filename))
        backup_zip = zipfile.ZipFile(zip_filename, 'w')

        # TODO: フォルダのツリーを渡り歩いてその中のファイルを圧縮する

    backup_to_zip("./target_folder")

if __name__ == '__main__':
    main()

