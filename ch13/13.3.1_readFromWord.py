#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import docx

    doc = docx.Document('demo.docx')
    print(len(doc.paragraphs))

    print(doc.paragraphs[0].text)
    print(doc.paragraphs[1].text)

if __name__ == '__main__':
    main()

