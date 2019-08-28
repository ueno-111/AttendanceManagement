from src.entity.item import Item

class ItemLogic(object):

    def __init__(self):
        self.itemList = [
            Item(),
            Item(),
            Item(),
            Item(),
            Item(),
            Item(),
            Item(),
            Item(),
            Item(),
            Item()
            ]

    def searchItemList(self):
        return self.itemList
