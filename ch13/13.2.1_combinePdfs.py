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

    # すべてのPDFファイルをループする
    for filename in pdf_files:
        with open(filename, 'rb') as pdf_file_obj:
            if "encrypted" in filename:
                # 暗号化されているPDFファイルは無視
                continue

            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            # 先頭を除くすべてのページをループして追加
            for page_num in range(1, len(pdf_reader.pages)):
                page_obj = pdf_reader.pages[page_num]
                pdf_writer.add_page(page_obj)
    # 結合したPDFをファイルに保存する
    with open('allminutes.pdf', 'wb') as pdf_output:
        pdf_writer.write(pdf_output)

if __name__ == '__main__':
    main()

