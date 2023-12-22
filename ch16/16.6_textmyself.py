#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
from twilio.rest import Client


def textmyself(message):
    account_SID = 'ACxxxxxxxxxxx'
    auth_token = 'xxxxxxxxxxxxxx'

    my_twilio_number = '+12345678901'
    my_cell_phone = '+819012345678'
    twilio_cli = Client(account_SID, auth_token)
    message = twilio_cli.messages.create(
        body='Come on',         # メッセージ本文
        from_=my_twilio_number, # 米国キャリアの携帯電話番号
        to=my_cell_phone        # 宛先となる携帯電話番号
    )

def main():
    textmyself('退屈な作業が終わったよ')


if __name__ == '__main__':
    main()
