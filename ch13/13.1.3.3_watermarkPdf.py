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

    pdf_writer = PyPDF2.PdfWriter() # 白紙のPDF文書を作成
    pdf_writer.add_page(minutes_first_page)
    for page_num in range(1, len(pdf_reader.pages)):
        # 透かしを埋め込んだ先頭以降のページをそのまま追加
        page_obj = pdf_reader.pages[page_num]
        pdf_writer.add_page(page_obj)

if __name__ == '__main__':
    main()

