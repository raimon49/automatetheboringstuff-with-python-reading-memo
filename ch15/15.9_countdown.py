#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import subprocess, time

    time_left = 60
    while time_left > 0:
        subprocess.Popen(['echo', str(time_left)])
        time.sleep(1)
        time_left = time_left - 1

    # カウントダウン後に完了を出力する
    subprocess.Popen(['printf', 'Exit\n'])


if __name__ == '__main__':
    main()
