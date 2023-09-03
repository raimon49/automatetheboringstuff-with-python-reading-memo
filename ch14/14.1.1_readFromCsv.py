#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import csv

    example_file = open('example.csv')
    example_reader = csv.reader(example_file)

if __name__ == '__main__':
    main()

