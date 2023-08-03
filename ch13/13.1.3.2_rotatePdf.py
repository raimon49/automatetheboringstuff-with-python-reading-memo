#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import PyPDF2

    minutes_file = open('meetingminutes.pdf', 'rb')
    pdf_reader = PyPDF2.PdfReader(minutes_file)
    page = pdf_reader.pages[0]
    page.rotate(90)

if __name__ == '__main__':
    main()

