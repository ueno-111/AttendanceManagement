# coding: UTF-8
from src.entity.item import Item
import datetime
#import mysql.connector

class ManagementService(object):
    '''
    勤怠管理画面
    '''

    def __init__(self):
        self.itemList = [
            Item(datetime.datetime(2019, 8, 28, 9, 55, 28), "遅刻", datetime.datetime(2019, 8, 28, 9, 55, 28), datetime.datetime(2019, 8, 28, 17, 55, 28), "出勤", "memo")
    def searchItemList(self):
        return self.itemList
