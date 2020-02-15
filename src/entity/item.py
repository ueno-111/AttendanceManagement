# coding: UTF-8
import datetime

class Item(object):

    def __init__(self, date, category, inttime, outtime, content, memo):
        self.date=date
        self.dateStr=self.date.strftime("%Y/%m/%d %H:%M:%S")
        self.category=category
        self.inttime=inttime if inttime else ''
        self.outtime=outtime if outtime else ''
        self.content=content if content else ''
        self.memo=memo if memo else ''
