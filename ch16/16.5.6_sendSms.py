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
        body='Come on',
        from_=my_twilio_number,
        to=my_cell_phone
    )


if __name__ == '__main__':
    main()
