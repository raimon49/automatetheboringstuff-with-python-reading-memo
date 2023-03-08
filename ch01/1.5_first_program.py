#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    print('Hello world!')
    print('What is your name?')
    my_name = input()
    print('It is good to meet you, ' + my_name)
    print('The length of your name is:')
    print(len(my_name))
    print('Wthat is your age?')
    my_age = input()
    print('You will be ' + str(int(my_age) + 1) + ' in a year.')

if __name__ == '__main__':
    main()
