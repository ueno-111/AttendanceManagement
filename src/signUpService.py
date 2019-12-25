# coding: UTF-8
import binascii
import requests
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
        CONFIG_FILE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"/setting.ini"

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
            db=DATABASE,
	    auth_plugin='mysql_native_password')

        # コネクションが切れた時に再接続してくれるよう設定
        # conn.ping(reconnect=True)

        # 接続できているかどうか確認
        print(conn.is_connected())

        # カーソルを取得する
        cur = conn.cursor()

        try:
            # SQL（データベースを操作するコマンド）を実行する
            # レコードの登録
            sql = 'insert into m_user (user_no, name, password, start_time, end_time, create_user, update_user) values (%s, %s, %s, "1000-01-01 00:00:00.000000", "9999-01-01 00:00:00.000000", "admin", "admin")'
            cur.execute(sql, (employeeNumber, username, password))  # 1件のみ
            conn.commit()
        except:
            conn.rollback()
            raise

        cur.close
        conn.close

        return True
