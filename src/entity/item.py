import datetime

class Item(object):

    def __init__(self, date, inout, name):
        self.date=date
        self.dateStr=self.date.strftime("%Y/%m/%d %H:%M:%S")
        self.inout=inout
        self.name=name
