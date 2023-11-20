#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import imapclient, ssl

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    imap_obj = imapclient.IMAPClient('imap.gmail.com',
                                     ssl=True,
                                     ssl_context=context)
    imap_obj.login('my_email_address@gmail.com', 'MY_PASS')
    imap_obj.select_folder('INBOX', readonly=True)

    UIDs = imap_obj.search(['SINCE', '05-Jul-2014'])


if __name__ == '__main__':
    main()
