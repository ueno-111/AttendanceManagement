# coding: UTF-8
from src.entity.item import Item
import datetime

class ManagementService(object):
    '''
    勤怠管理画面
    '''

    def __init__(self):
        self.itemList = [
            Item(datetime.date(2019, 8, 28), "", datetime.time(9, 55, 28), datetime.time(18, 0, 28)),
            Item(datetime.date(2019, 8, 29), "", datetime.time(9, 55, 28), datetime.time(18, 0, 28))
            ]

    def searchItemList(self):
        return self.itemList
