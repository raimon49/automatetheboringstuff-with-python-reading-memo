#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from twilio.rest import Client


    account_SID = 'ACxxxxxxxxxxx'
    auth_token = 'xxxxxxxxxxxxxx'
    twilio_cli = Client(account_SID, auth_token)

    my_twilio_number = '+12345678901'
    my_cell_phone = '+819012345678'
    message = twilio_cli.messages.create(
        body='Come on',         # メッセージ本文
        from_=my_twilio_number, # 米国キャリアの携帯電話番号
        to=my_cell_phone        # 宛先となる携帯電話番号
    )

    # 作成されたmessageオブジェクトを確認
    print(message.to)     # '+12345678901'
    print(message.from_)  # '+819012345678'
    print(message.body)   # 'Come on'
    print(message.status) # 'queued'
    print(message.sid)    # 'SM09520de7639ba3af137c6fcb7c5f4b51'

    # 最新情報のmessageオブジェクトを取得
    updated_message = twilio_cli.messages.get(message.sid)
    print(updated_message.status)    # 'sending' or 'sent' or 'delivered' or 'undelivered' or 'failed'
    print(updated_message.date_sent) # datetime.datetime(2015, 7, 8, 1, 36, 18)


if __name__ == '__main__':
    main()
