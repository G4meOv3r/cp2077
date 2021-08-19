from random import seed, randint, uniform
from math import ceil
from Gameplay.Items.Items import Items

class Shop:
    def __init__(self, info):
        itm = Items()
        if info == "resources":
            scrap_price_buy = randint(5, 15)
            scrap_price_cell = scrap_price_buy+randint(1,5)
            mine_price_buy = randint(70,100)
            mine_price_cell = mine_price_buy+randint(1,15)
            self.products = [itm.SCRAP, itm.MINERALS]
            self.text = ["a", "b"]
            self.prices[[scrap_price_buy,scrap_price_cell],[mine_price_buy,mine_price_cell]]