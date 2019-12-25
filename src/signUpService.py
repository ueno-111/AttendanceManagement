# coding: UTF-8
import hashlib
from src.connector import Connector


class SignUpService(object):
    '''
    新規登録画面
    '''

    def __init__(self):
        pass


    def registerAction(self, employeeNumber, username, userid, password):

        con = Connector()
        def func():
                sql = 'insert into m_user (user_no, display_name, name, password, create_user, update_user) values (%s, %s, %s, %s, "admin", "admin")'
                con.registerAction(sql, (employeeNumber, username, userid, hashlib.sha256(password.encode('utf-8')).hexdigest()))
                sql = 'select user_id, user_no, name from m_user where name = %s'
                user = con.selectOne(sql, (username,))
                # カード登録用レコード登録
                sql = 'insert into m_card (user_id, create_user, update_user) values (%s, "admin", "admin")'
                param = (user["user_id"],)
                con.registerAction(sql, param)

        con.transactionAction(func)

        return True
