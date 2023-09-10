#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import csv

    example_file = open('example.csv')
    example_reader = csv.reader(example_file)
    example_data = list(example_reader)
    print(example_data, end='\n\n') # [['4/5/2014 13:34', 'Apples', '73'], ['4/5/2014 3:41', 'Cherries', '85'],...

    print(example_data[0][0]) # 4/5/2014 13:34
    print(example_data[0][1]) # Apples
    print(example_data[0][2]) # 73

    print(example_data[1][1]) # Cherries
    print(example_data[6][1]) # Strawberries

    print()
    i = 0
    for row in csv.reader(open('example.csv')): # enumerate indexが進んでいるから再度読み込み直す
        print('Row #' + str(i) + ' ' + str(row))
        i = i + 1

    # Windowsでは1行空きになってしまうのを防ぐため引数newline=''を指定して開く
    with open('output.csv', 'w', newline='') as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
        output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
        output_writer.writerow([1, 2, 3.141592, 4])

    with open('example.tsv', 'w', newline='') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter='\t',
                                lineterminator='\n\n')
        tsv_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
        tsv_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
        tsv_writer.writerow([1, 2, 3.141592, 4])



if __name__ == '__main__':
    main()

