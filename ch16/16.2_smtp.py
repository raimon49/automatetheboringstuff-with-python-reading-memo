#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import smtplib

    smtp_obj = smtplib.SMTP('smtp.example.com', 587)
    print(smtp_obj.ehlo())
    print(smtp_obj.starttls())
    smtp_obj.quit()


if __name__ == '__main__':
    main()
