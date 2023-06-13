#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import  bs4

    example_file = open('example.html')
    example_soup = bs4.BeautifulSoup(example_file)

    # 属性の探索
    elems = example_soup.select('#author')
    print(type(elems))
    print(len(elems))
    print(type(elems[0]))
    print(elems[0].getText())
    print(str(elems[0]))
    print(elems[0].attrs)

    # タグの探索
    p_elems = example_soup.select('p')
    print(len(p_elems))
    print(str(p_elems[0]))
    print(p_elems[0].getText())
    print(str(p_elems[1]))
    print(p_elems[1].getText())
    print(str(p_elems[2]))
    print(p_elems[2].getText())

    # Tagオブジェクトのget()メソッドを用いた探索
    span_elem = example_soup.select('span')[0]
    print(str(span_elem))
    print(span_elem.get('id'))

if __name__ == '__main__':
    main()

