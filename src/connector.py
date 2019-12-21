# coding: UTF-8
import binascii
import hashlib
import mysql.connector as mydb
import configparser
import os


class Connector(object):
    '''
    mysql-connect
    '''

    # setting.iniから接続情報の取得
    CONFIG_FILE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "setting.ini"

    print("MYSQL接続設定ファイル : " + CONFIG_FILE)

    conf = configparser.SafeConfigParser()
    conf.read(CONFIG_FILE)

    HOST     = conf.get('connection', 'host')
    PORT     = conf.get('connection', 'port')
    USERNAME = conf.get('connection', 'user')
    PASSWORD = conf.get('connection', 'password')
    DATABASE = conf.get('connection', 'database')
    # 接続する
    conn = mydb.connect(
        host=HOST,
        port=PORT,
        user=USERNAME,
        passwd=PASSWORD,
        db=DATABASE)
    # コネクションが切れた時に再接続してくれるよう設定
    conn.ping(reconnect=True)

    def __init__(self,auto_commit=False):
        # 接続できているかどうか確認
        print(Connector.conn.is_connected())
        # カーソルを取得する
        self.cur = Connector.conn.cursor(dictionary=True)
        self.auto_commit = auto_commit
        pass

    def __del__(self):
        self.cur.close


    def transactionAction(self, func):
        self.auto_commit = False
        try:
            func()
            Connector.conn.commit()
        except:
            Connector.conn.rollback()
            raise

    def registerAction(self, sql, data):

        try:
            # SQL（データベースを操作するコマンド）を実行する
            # レコードの登録
            self.cur.execute(sql, data)  # 1件のみ
            if self.auto_commit:
                Connector.conn.commit()
        except:
            Connector.conn.rollback()
            raise

        return True

    def selectAll(self, sql, data):

        self.cur.execute(sql, data)
        data = self.cur.fetchall()

        return data

    def selectOne(self, sql, data):

        self.cur.execute(sql, data)
        data = self.cur.fetchone()

        return data