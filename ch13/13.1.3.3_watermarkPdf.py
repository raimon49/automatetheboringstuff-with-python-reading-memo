#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import PyPDF2

    minutes_file = open('meetingminutes.pdf', 'rb')
    pdf_reader = PyPDF2.PdfReader(minutes_file)
    minutes_first_page = pdf_reader.pages[0]
    pdf_watermark_reader = PyPDF2.PdfReader(open('watermark.pdf', 'rb'))
    # 別PDFのページを重ねて透かしを埋め込む
    minutes_first_page.merge_page(pdf_watermark_reader.pages[0])

if __name__ == '__main__':
    main()

