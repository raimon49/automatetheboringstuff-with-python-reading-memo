#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import smtplib

    # GmailのSMTPサーバーに接続
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    print(type(smtp_obj))

    # GmailのSMTPサーバーにTLS接続
    # smtp_ssl = smtplib.SMTP_SSL('smtp.gmai.com', 465)
    # print(type(smtp_ssl))


if __name__ == '__main__':
    main()
