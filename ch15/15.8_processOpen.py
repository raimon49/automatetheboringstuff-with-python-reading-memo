#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import subprocess, sys

    proc = subprocess.Popen('/usr/bin/ls') # <Popen: returncode: None args: '/usr/bin/ls'>
    print(proc.poll() == None) # True
    print(proc.wait())         # 0
    print(proc.poll())         # 0

    subprocess.Popen(['/usr/bin/ls', '/usr/bin']) # Popenで呼び出す外部コマンドに引数を渡す（ls /usr/bin）

    # subprocess.Popen([sys.executable, '../ch01/1.5_first_program.py']) # 外部Pythonスクリプトの実行


if __name__ == '__main__':
    main()
