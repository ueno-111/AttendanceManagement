# coding: UTF-8
import binascii
import nfc
import requests
import hashlib
import mysql.connector as mydb
import configparser
import os


class SignUpService(object):
    '''
    新規登録画面
    '''

    def __init__(self):
        pass


    def registerAction(self, employeeNumber, username, password):

        # setting.iniから接続情報の取得
        CONFIG_FILE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + "\\setting.ini")

        print(CONFIG_FILE)

        # conf = configparser.SafeConfigParser()
        # conf.read(CONFIG_FILE)

        # USERNAME = conf.get('connection', 'user')
        # PASSWORD = conf.get('connection', 'password')
        # SERVER   = conf.get('connection', 'server')
        # DATABASE = conf.get('connection', 'database')

        # 接続する
        conn = mydb.connect(
            host="35.209.236.130",
            port='3306',
            user='py',
            passwd='pyPY0000/',
            db='attendance')

        # コネクションが切れた時に再接続してくれるよう設定
        # conn.ping(reconnect=True)

        # 接続できているかどうか確認
        print(conn.is_connected())

        # カーソルを取得する
        cur = conn.cursor()

        # SQL（データベースを操作するコマンド）を実行する
        # レコードの登録
        sql = 'insert into m_user (user_no, name, password) values (%s, %s, %s)'
        c.execute(sql, (employeeNumber, username, password))  # 1件のみ
        # datas = [
        #     (2, 'foo'),
        #     (3, 'bar')
        # ]
        # c.executemany(sql, datas)    # 複数件
        # print('\n* レコードを3件登録\n')

        cur.close
        conn.close

        return True
