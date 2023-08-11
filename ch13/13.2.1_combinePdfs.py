#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import PyPDF2, os

    # すべてのPDFファイル名を取得する
    pdf_files = []
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdf_files.append(filename)
            pdf_files.sort(key=str.lower)

    pdf_writer = PyPDF2.PdfWriter()

    # TODO: すべてのPDFファイルをループする
    # TODO: 先頭を除くすべてのページをループして追加する
    # TODO: 結合したPDFをファイルに保存する

if __name__ == '__main__':
    main()

