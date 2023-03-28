#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
import random

def main():
    def eggs(some_parameter):
        some_parameter.append('Hello')

    spam = [1, 2, 3]
    eggs(spam)
    print(spam)

if __name__ == '__main__':
    main()

