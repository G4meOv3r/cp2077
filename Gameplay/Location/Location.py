from random import seed, randint, uniform
from math import ceil

class Location:
    def __init__(self, cords):
        self.cords = cords
        self.seed, self.events_seed = self.__seeds()
        seed(self.seed)
        
        
    def __seeds(self):
        for i in range(3):
            loc_seed += ord(self.cords[i]-65)**i
        loc_seed*=int(self.cords[4])*int(self.cords[5])
        return (loc_seed, ceil(loc_seed/randint(int(self.cords[4]), int(self.cords[5]))))
        
    def __generate_location(self):
        if uniform(0,1) < 0.5:
            station = Station(self.events_seed)
            