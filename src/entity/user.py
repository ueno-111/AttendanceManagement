from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,id,password):
        self.id = id
        self.password = password

    def getid(self):
        return self.id

    def matchUser(self, id, password):
        return self.id == id and self.password == password

    def matchPassword(self,password):
        return self.password == password

    def __eq__(self, other):
        '''== のオーバーライド'''
        return self.matchUser(other.id,other.password)
