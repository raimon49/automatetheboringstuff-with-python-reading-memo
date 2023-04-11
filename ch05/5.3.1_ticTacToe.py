#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    # 三目並べのデータ構造
    the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    def print_board(board):
        # ゲーム状況の出力
        print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
        print('-+-+-')
        print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
        print('-+-+-')
        print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

    turn = 'X'
    for i in range(9):
        print_board(the_board)
        print(turn + 'の番です。どこに打つ？')
        move = input()
        the_board[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


if __name__ == '__main__':
    main()

