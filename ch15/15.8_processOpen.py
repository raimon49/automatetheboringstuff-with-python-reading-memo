#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import subprocess

    proc = subprocess.Popen('/usr/bin/ls') # <Popen: returncode: None args: '/usr/bin/ls'>
    print(proc.poll() == None) # True
    print(proc.wait())


if __name__ == '__main__':
    main()
