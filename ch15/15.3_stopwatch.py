#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import time

    print('Enterを押すと開始します。その後、Enterを押せば経過時間を表示します。Ctrl + Cで終了します。')
    input()
    print('スタート')
    start_time = time.time()
    last_time = start_time
    lap_num = 1

if __name__ == '__main__':
    main()
