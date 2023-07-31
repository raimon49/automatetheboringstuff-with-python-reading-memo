#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import PyPDF2

    pdf1_file = open('meetingminutes.pdf', 'rb')
    pdf2_file = open('meetingminutes2.pdf', 'rb')
    pdf1_reader = PyPDF2.PdfReader(pdf1_file)
    pdf2_reader = PyPDF2.PdfReader(pdf2_file)

    pdf_writer = PyPDF2.PdfWriter()
    for page_num in range(len(pdf1_reader.pages)):
        page_obj = pdf1_reader.pages[page_num]
        pdf_writer.add_page(page_obj)

if __name__ == '__main__':
    main()

