#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import pyautogui

    # 解像度をタプルで取得し出力・変数に代入
    print(pyautogui.size())
    width, height = pyautogui.size()

    # マウスポインタを(0, 0)を限定とする絶対座標で4分の1秒ずつ移動
    for i in range(10):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)

    # 現在位置からの相対座標でマウスポインタを4分の1秒ずつ移動
    for i in range(10):
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)

    # マウスの座標をタプルで取得
    print(pyautogui.size()) # (311, 622)

if __name__ == '__main__':
    main()
