from src.entity.user import User

class UserLogic(object):

    def __init__(self):
        self.userDict = {"fumiya.sugiyama":User("fumiya.sugiyama","12345")}

    def searchUser(self,username):
        if username not in self.userDict:
            return
        return self.userDict[username]
