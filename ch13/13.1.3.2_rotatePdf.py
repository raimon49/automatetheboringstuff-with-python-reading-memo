#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import PyPDF2

    minutes_file = open('meetingminutes.pdf', 'rb')
    pdf_reader = PyPDF2.PdfReader(minutes_file)
    page = pdf_reader.pages[0]
    page.rotate(90)

    pdf_writer = PyPDF2.PdfWriter() # 白紙のPDF文書を作成
    pdf_writer.add_page(page)

    with open('rotatedPage.pdf', 'wb') as result_pdf_file:
        # 新規PDFファイルとして保存
        pdf_writer.write(result_pdf_file)
        minutes_file.close()

if __name__ == '__main__':
    main()

