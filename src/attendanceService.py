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

        con = Connector()
        def func():
                sql = 'select * from m_user where card_no = %s'
                user = con.selectOne(sql, (cardId,))

		if(user is not None):
#			sql = 'insert t_attendance (user_id, target_date, in_time, out_time)'
			return 1
		elif:
			return 0 			

#        con.transactionAction(func)

#        return random.randint(0, 1)
