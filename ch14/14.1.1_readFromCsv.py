#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import csv

    example_file = open('example.csv')
    example_reader = csv.reader(example_file)
    example_data = list(example_reader)
    print(example_data, end='\n\n') # [['4/5/2014 13:34', 'Apples', '73'], ['4/5/2014 3:41', 'Cherries', '85'],...

if __name__ == '__main__':
    main()

