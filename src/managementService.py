# coding: UTF-8
from src.entity.item import Item
from src.connector import Connector
import datetime

class ManagementService(object):
    '''
    勤怠管理画面
    '''

    def __init__(self):
        pass

    def searchItemList(self,userNo):
        con = Connector()
        sql = 'SELECT user_id FROM m_user WHERE user_no = %s'
        user = con.selectOne(sql, (userNo,))
        userId = user['user_id']
        sql = 'SELECT target_date,category,in_time,out_time,work_context,memo FROM t_attendance WHERE user_id = %s'
        list = con.selectAll(sql, (userId,))
        return [Item(
            i['target_date'],
            i['category'],
            i['in_time'],
            i['out_time'],
            i['work_context'],
            i['memo']
        ) for i in list]
