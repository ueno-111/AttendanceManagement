# coding: UTF-8
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,user_no,name):
        self.user_no = user_no
        self.name = name

    def getuser_no(self):
        return self.user_no

    def get_id(self):
        return self.name
