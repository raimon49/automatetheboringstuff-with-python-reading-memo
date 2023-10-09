#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import time

    print('Enterを押すと開始します。その後、Enterを押せば経過時間を表示します。Ctrl + Cで終了します。')
    input()
    print('スタート')
    start_time = time.time() # 最初のラップ開始時間
    last_time = start_time
    lap_num = 1

    # ラップタイムを計測する
    try:
        while True:
            input()
            now = time.time() # Enterキーが入力される度にラップタイムを計算
            lap_time = round(now - last_time, 2)    # 小数点第2位まで丸める
            total_time = round(now - start_time, 2) # 小数点第2位まで丸める
            print('ラップ #{}: {} ({})'.format(
                lap_num,
                total_time,
                lap_time),
            end='')
            lap_num += 1
            last_time = now # ラップタイムをリセット
    except KeyboardInterrupt:
        # Ctrl + Cで割り込まれたら終了する
        print('\n終了')

if __name__ == '__main__':
    main()
