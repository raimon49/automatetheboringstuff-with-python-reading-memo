#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import pyautogui

    # 解像度をタプルで取得し出力・変数に代入
    print(pyautogui.size())
    width, height = pyautogui.size()

    for i in range(10):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)


if __name__ == '__main__':
    main()
