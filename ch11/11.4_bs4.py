#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import  bs4

    example_file = open('example.html')
    exemple_soup = bs4.BeautifulSoup(example_file)
    elems = exemple_soup.select('#author')
    print(type(elems))
    print(len(elems))
    print(type(elems[0]))
    print(elems[0].getText())
    print(str(elems[0]))
    print(elems[0].attrs)

if __name__ == '__main__':
    main()

