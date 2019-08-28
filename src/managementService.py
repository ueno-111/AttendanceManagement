from src.entity.item import Item
import datetime

class ManagementService(object):
    '''
    勤怠管理画面
    '''

    def __init__(self):
        self.itemList = [
            Item(datetime.datetime(2019, 8, 28, 9, 55, 28), "出勤", "杉山"),
            Item(datetime.datetime(2019, 8, 28, 19, 0, 0), "退勤", "杉山"),
            Item(datetime.datetime.today(), "出勤", "上野"),
            Item(datetime.datetime.today() + datetime.timedelta(hours=8), "退勤", "上野")
            ]

    def searchItemList(self):
        return self.itemList
