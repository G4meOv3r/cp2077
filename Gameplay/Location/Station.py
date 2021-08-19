from random import seed, randint, uniform
from math import ceil
from Gameplay.Location.Shop import Shop
from Gameplay.Player.Player import Player

class Station:
    def __init__(self, seed):
        plr = Player()
        seed(seed)
        if plr.use_luck(uniform(0,1), "positive") < 0.4:
            self.res = Shop("resources")