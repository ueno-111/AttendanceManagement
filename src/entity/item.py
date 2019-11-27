# coding: UTF-8
import datetime

class Item(object):

    def __init__(self, date, category, inttime, outtime, content, memo):
        self.date=date
        self.dateStr=self.date.strftime("%Y/%m/%d %H:%M:%S")
        self.category=category
        self.inttime=inttime
        self.outtime=outtime
        self.content=content
        self.memo=memo
