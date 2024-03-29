#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import threading, time

    print('プログラム開始')

    def take_a_nap():
        time.sleep(5)
        print('起きた!')

    thread_obj = threading.Thread(target=take_a_nap)
    thread_obj.start() # take_a_nap関数を新しいスレッドで実行開始

    print('プログラム終了')

    # プログラム開始
    # プログラム終了
    # 起きた!


if __name__ == '__main__':
    main()
