#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import requests, os, bs4

    res = requests.get('https://xkcd.com')
    res.raise_for_status()


if __name__ == '__main__':
    main()

