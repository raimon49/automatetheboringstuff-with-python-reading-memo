#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import PyPDF2

    pdf1_file = open('meetingminutes.pdf', 'rb')
    pdf2_file = open('meetingminutes2.pdf', 'rb')
    pdf1_reader = PyPDF2.PdfReader(pdf1_file)
    pdf2_reader = PyPDF2.PdfReader(pdf2_file)

    pdf_writer = PyPDF2.PdfWriter() # 白紙のPDF文書を作成
    for page_num in range(len(pdf1_reader.pages)):
        page_obj = pdf1_reader.pages[page_num]
        # ページをコピー
        pdf_writer.add_page(page_obj)

    for page_num in range(len(pdf2_reader.pages)):
        page_obj = pdf2_reader.pages[page_num]
        # ページをコピー
        pdf_writer.add_page(page_obj)

    with open('combinedminutes.pdf', 'wb') as pdf_output_file:
        # 新規PDFファイルとして保存
        pdf_writer.write(pdf_output_file)
        pdf1_file.close()
        pdf2_file.close()

if __name__ == '__main__':
    main()

