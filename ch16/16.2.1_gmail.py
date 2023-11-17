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

    print(smtp_obj.ehlo())     # (250, b'smtp.gmail.com at your service, [114.152.124.80]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
    print(smtp_obj.starttls()) # (220, b'2.0.0 Ready to start TLS')

    # print(smtp_obj.login('my_email_address@gmail.com', 'MY_PASS')) # (235, b'2.7.0 Accepted')
    # print(smtp_obj.sendmail('my_email_address@gmail.com',
    #                         'recipient@example.com',
    #                         'Subject: Solong.\nDearAlice, so long and thanks for all the fish. Sincerely, Bob'))

    # 日本語のメール送信
    from email.mime.text import MIMEText
    from email.header import Header

    # charset = 'iso-2022-jp'
    # msg = MIMEText('日本語の全文', 'plain', charset)
    # msg['Subject'] = Header('日本語の件名'.encode(charset), charset)

    # smtp_obj = smtplib.SMTP('smtp.example.com', 587)
    # smtp_obj.ehlo()
    # smtp_obj.starttls()
    # smtp_obj.login('my_email_address@example.com', 'MY_PASS')
    # smtp_obj.sendmail('my_email_address@example.com', 'to@example.com' msg.as_string())

    # GmailのSMTPサーバーから切断
    smtp_obj.quit()


if __name__ == '__main__':
    main()
