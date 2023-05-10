#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    sonnet_file = open('sonnet29.txt')
    lines = sonnet_file.readlines()

    print(lines) # 各行の末尾には改行文字\nが付いている
    print()
    print('\n'.join(lines))

    # path/fileの確認
    import os

    assert not os.path.isabs('.')
    assert os.path.isabs(os.path.abspath('.'))
    assert os.path.exists('.')
    assert os.path.isdir('.')

if __name__ == '__main__':
    main()

