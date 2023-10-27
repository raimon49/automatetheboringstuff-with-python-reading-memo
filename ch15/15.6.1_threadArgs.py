#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import threading

    thread_obj = threading.Thread(
        target=print,
        args=['Cats', 'Dogs', 'Frogs'],
        kwargs={'sep': ' & '}
    )
    thread_obj.start()


if __name__ == '__main__':
    main()
