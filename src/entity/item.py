# coding: UTF-8
import datetime

class Item(object):

    def __init__(self, date, workType="", inTime=None, outTime=None, workContent="", memo=""):
        self.date=date
        self.dateStr=self.date.strftime("%Y/%m/%d")
        self.workType=workType
        self.inTime=inTime
        if self.inTime is not None:
            self.inTimeStr=self.inTime.strftime("%H:%M:%S")
        self.outTime=outTime
        if self.outTime is not None:
            self.outTimeStr=self.outTime.strftime("%H:%M:%S")
        self.workContent=workContent
        self.memo=memo
