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

    # 2015年1月の未読メールを検索（2015-01-01は含まれるが2015-02-01は含まれない）
    UIDs = imap_obj.search(['SINCE', '01-Jan-2015', 'BEFORE',
                            '01-Feb-2015', 'UNSEEN'])

    # 2015年1月1日以降にaliceから届いた全てのメールを検索
    UIDs = imap_obj.search(['SINCE', '01-Jan-2015', 'FROM',
                            'alice@example.com'])

    # 2015年1月1日以降にalice以外から届いた全てのメールを検索
    UIDs = imap_obj.search(['SINCE', '01-Jan-2015', 'NOT', 'FROM',
                            'alice@example.com'])

    # aliceまたはbobから受信したメールを全て検索
    UIDs = imap_obj.search('OR', 'FROM', 'alice@example.com',
                           'FROM', 'bob@example.com')

    # メールには1つのFromヘッダーしか無いので、1つも検索条件にマッチしない
    UIDs = imap_obj.search('FROM', 'alice@example.com', # UIDs = []
                           'FROM', 'bob@example.com')

    # Gmailの高度な検索エンジンを使った検索
    UIDs = imap_obj.gmail_search('meaning of life')

    raw_massages = imap_obj.fetch(UIDs, ['BODY[]'])

    imap_obj.logout()


if __name__ == '__main__':
    main()
