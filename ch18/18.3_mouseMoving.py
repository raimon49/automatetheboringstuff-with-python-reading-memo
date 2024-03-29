#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import pyautogui, pyperclip

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
    print(pyautogui.position()) # (311, 622)

    # マウス座標を取得して表示し続ける
    while True:
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(position, end='')
        print('\b' * len(position_str), end='', flush=True) # バックスペース文字の出力時はflush=Trueにしないと正しく表示されない

    # 画面座標の左上をクリックさせる
    pyautogui.click(10, 5)
    pyautogui.rightClick(10, 5)  # 右ボタンをクリック
    pyautogui.middleClick(10, 5) # 中央ボタンをクリック

    # クリック位置から相対的にマウス位置を移動させる
    distance = 200
    while distance > 0: # 四角形の渦巻き状にドラッグするループ
        pyautogui.dragRel(distance, 0, duration=0.2)  # 右へ移動
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2)  # 下へ移動
        pyautogui.dragRel(-distance, 0, duration=0.2) # 左へ移動
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=0.2) # 上へ移動

    # マウスホイールをスクロール
    pyautogui.scroll(200)

    numbers = ''
    for i in range(200):
        numbers = numbers + str(i) + '\n'

    pyperclip.copy(numbers) # 200までの数字を改行で繋げてクリップボードにコピー

    # スクリーンショットを取得（Imageオブジェクトで返される）
    im = pyautogui.screenshot()
    # Imageオブジェクトに座標タプルを指定してgetpixel()を呼ぶとRGBタプルが返される
    print(im.getpixel((0, 0)))    # (130, 135, 144)
    print(im.getpixel((50, 200))) # (255, 135, 144)

if __name__ == '__main__':
    main()
