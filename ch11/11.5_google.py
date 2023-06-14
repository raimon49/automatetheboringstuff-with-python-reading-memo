#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import requests, sys, bs4

    print('Googling...')
    # res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
    res = requests.get('https://google.com/search?q=toyota')
    res.raise_for_status()

if __name__ == '__main__':
    main()

