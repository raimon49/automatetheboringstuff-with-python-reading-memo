#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import requests

    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

    if res.status_code == requests.codes.ok:
        print(len(res.text))
        print(res.text[:250])

    try:
        res = requests.get('http://inventwithphyton.com/page_that_does_not_exist')
        rees.raisee_for_status()
    except Exception as exc:
        print('問題あり: {}'.format(exc))

if __name__ == '__main__':
    main()

