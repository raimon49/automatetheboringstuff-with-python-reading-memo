#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import PyPDF2

    # PdfReaderオブジェクトを生成
    pdf_file_obj = open('meetingminutes.pdf', 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(0, len(pdf_reader.pages)):
        # 全てのページをコピー
        page_obj = pdf_reader.pages[page_num]
        pdf_writer.add_page(page_obj)

    # PDFユーザーパスワード/オーナーパスワードを同じ文字列で設定
    pdf_writer.encrypt('sowrdfish')
    with open('encryptedminutes.pdf', 'wb') as result_pdf:
        pdf_writer.write(result_pdf)

if __name__ == '__main__':
    main()

