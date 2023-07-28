#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import PyPDF2

    # PdfReaderオブジェクトを生成
    pdf_file_obj = open('encrypted.pdf', 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

    print(pdf_reader.is_encrypted)

if __name__ == '__main__':
    main()

