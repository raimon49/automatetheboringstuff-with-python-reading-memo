#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    market_2nd = {'ns': 'green', 'ew': 'red'}
    mission_16th = {'ns': 'red', 'ew': 'green'}

    def switch_lights(stoplight):
        for key in stoplight.keys():
            if stoplight[key] == 'green':
                stoplight[key] = 'yellow'
            elif stoplight[key] == 'yellow':
                stoplight[key] = 'red'
            elif stoplight[key] == 'red':
                stoplight[key] = 'green'

        assert 'red' in stoplight.values(), '赤信号がない! ' + str(stoplight)

    switch_lights(market_2nd)

if __name__ == '__main__':
    main()

