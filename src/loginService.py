# coding: UTF-8
import hashlib
from src.entity.user import User
from flask import Flask, request
from src.connector import Connector

class LoginService(object):
    '''
    ログイン処理
    '''

    def __init__(self):
        pass

    def loginUser(self,username,password):
        sql = 'select user_no, name from m_user where name = %s and password = %s'
        user = Connector().selectOne(sql, (username, hashlib.sha256(password.encode('utf-8')).hexdigest()))
        if not user:
            return None
        else:
            return User(user['user_no'],user['name'])

    def searchUser(self,username):
        sql = 'select user_no, name from m_user where name = %s'
        user = Connector().selectOne(sql, (username,))
        if not user:
            return None
        else:
            return User(user['user_no'],user['name'])