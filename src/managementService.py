# coding: UTF-8
from src.entity.item import Item
#from src.connector import Connector
import datetime

class ManagementService(object):
    '''
    勤怠管理画面
    '''

    def __init__(self):
        self.itemList = [
       Item(datetime.datetime(2019, 8, 28, 9, 55, 28), "遅刻", datetime.datetime(2019, 8, 28, 9, 55, 28), datetime.datetime(2019, 8, 28, 17, 55, 28), "出勤", "memo")]
    
    def searchItemList(self):
        return self.itemList

    def searchItemList2(self,userId):
        con = Connector()
        sql = 'SELECT target_date,category,in_time,out_time,work_context,memo FROM t_attendance WHERE user_id = "useriId"'
        return con.selectAll(sql)
        # return self.itemList
