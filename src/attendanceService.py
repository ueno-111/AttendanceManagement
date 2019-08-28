# coding: UTF-8
import random

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
        return random.randint(0, 1)
