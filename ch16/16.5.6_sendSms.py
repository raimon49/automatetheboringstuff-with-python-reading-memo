#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    from twilio.rest import Client


    account_SID = 'ACxxxxxxxxxxx'
    auth_token = 'xxxxxxxxxxxxxx'
    twilio_cli = Client(account_SID, auth_token)


if __name__ == '__main__':
    main()
