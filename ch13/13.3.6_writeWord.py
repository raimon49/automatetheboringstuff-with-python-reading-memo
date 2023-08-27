#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import docx

    doc = docx.Document()
    doc.add_paragraph('Hello world!!')

    # doc.save('helloworld.docx')

    para_obj1 = doc.add_paragraph('これは第2段落です')
    para_obj2 = doc.add_paragraph('これは第3段落です')
    para_obj1.add_run(' これは第2段落に追加したテキストです。')

    doc.save('multipuleParagraphs.docx')

if __name__ == '__main__':
    main()

