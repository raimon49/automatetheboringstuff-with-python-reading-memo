#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    cat_names = []
    while True:
        print('猫' + str(len(cat_names) + 1) + 'の名前を入力してください' +
              '（終了するにはEnterキーだけ押してください）')
        name = input()
        if name == '': # Enterキーだけ押されて何も入力されていない
            break
        cat_names = cat_names + [name] # リストの連結
    print('猫の名前は次のとおり:')
    for name in cat_names:
        print('  ' + name)

if __name__ == '__main__':
    main()

