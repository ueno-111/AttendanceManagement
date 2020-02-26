# coding: UTF-8
import random
import datetime
import time
from src.connector import Connector

class AttendanceService(object):
    '''
    カードリーダーとの送受信処理
    '''

    def __init__(self):
        pass

    def existIdAndAttendance(self,cardId):
        '''
        IDが存在するかチェックして存在したら出退勤も行う
        '''

        con = Connector(True)
        sql = 'select * from m_card where card_no = %s'
        card = con.selectOne(sql, (cardId,))

        if(card is not None):
            # カードIDが登録されていたら出勤or退勤を登録            
            return self.inOutAttendance(card, con)

        sql = 'select * from m_card where card_no is null'
        card = con.selectOne(sql)
        if(card is not None):
            # カードID登録待ちのデータがあればカードIDを登録           
            return self.registCard(card, con, cardId)
        # 該当するカードIDがないため0を返す
        return 0 			

    def inOutAttendance(self, card, con):
        '''
        出勤or退勤を登録 
        '''
        
        sql = 'select * from t_attendance where user_id = %s and target_date = %s'
        attendance = con.selectOne(sql, (card['user_id'], datetime.date.today()))
        if(attendance is None):
            # 本日付のデータがない場合は出勤データinsert
            sql = 'insert t_attendance (user_id, target_date, category, in_time, create_user, update_user) values (%s, %s, %s, %s, %s, %s)'
            con.registerAction(sql, (card['user_id'], time.strftime('%Y-%m-%d'), 0, time.strftime('%H:%M:%S'), 'admin', 'admin'))
            return 1
        
        if(attendance['out_time'] is None):
            # 本日付けの出勤データがある場合は退勤データをupdate
            sql = 'update t_attendance set out_time = %s, update_user = %s where attendance_id = %s'
            con.registerAction(sql, (time.strftime('%H:%M:%S'), 'admin', attendance['attendance_id']))
            return 1
        
        # すでに本日付の出退勤データがある場合は０を返す
        return 0
    
    def registCard(self, card, con, cardId):
        '''
        カードIDを登録 
        '''
        sql = 'update m_card set card_no = %s, update_user = %s where card_id = %s'
        con.registerAction(sql, (cardId, 'admin', card['card_id']))

        return 1