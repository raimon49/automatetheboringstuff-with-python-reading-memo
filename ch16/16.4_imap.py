#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import imapclient, ssl

    # IMAPサーバーに接続
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    imap_obj = imapclient.IMAPClient('imap.gmail.com',
                                     ssl=True,
                                     ssl_context=context)

    # IMAPサーバーにログイン
    imap_obj.login('my_email_address@gmail.com', 'MY_PASS')

    # フォルダを選択
    folders = imap_obj.list_folders()
    imap_obj.select_folder('INBOX', readonly=True)

    # 2014年7月5日以降のメールを検索
    UIDs = imap_obj.search(['SINCE', '05-Jul-2014'])

    # 選択中フォルダの全てのメールを取得
    UIDs = imap_obj.search(['ALL'])

    # 2015年7月5日の全てのメールを検索
    UIDs = imap_obj.search(['ON', '05-Jul-2014'])

    imap_obj.logout()


if __name__ == '__main__':
    main()
