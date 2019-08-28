# coding: UTF-8
from src.entity.user import User

class LoginService(object):
    '''
    ログイン処理
    '''

    def __init__(self):
        pass

    def searchUser(self,username):
        userDict = {"pe":User("pe","pe")}
        if username not in userDict:
            return
        return userDict[username]
