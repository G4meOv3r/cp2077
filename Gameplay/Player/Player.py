from math import ceil

class PlayerMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
        
class Player(metaclass=ConsoleMeta):
    def __init__(self):
        self.__stats = {"str": 0, "agl": 0, "int": 0, "adv": 0, "lck": 0}
        self.__inventory = []
        self.__equipment = {"ammor": None, "weapons": None}
        self.__max_hp = 10
        self.__hp = 10
    
    def change_stats(self, delta):
        for i in range(delta):
            self.__stats[delta[i]["stat"]]+=delta[i]["change"]
            
    def set_stats(self, info):
        for i in range(info):
            self.__stats[info[i]["stat"]] = info[i]["val"]
    
    def check_stats(self, stats):
        for i in range(stats):
            if self.__stats[stats[i]["stat"]] < stats[i]["val"]:
                return False
        return True
    
    def item_to_filter(self, item, bad_keys):
        filters = []
        keys = list(items.keys())
        for i in range(len(keys)):
            if not(keys[i] in bad_keys):
                filters.append({"type": "key": keys[i],"val": item[keys[i]]})
        return filters
    
    def return_items(self, filters, pos):
        result = []
        result_pos = []
        for i in range(self.__inventory):
            try:
                for j in range(filters):
                    if filters[j]["type"] == "==":
                        if self.__inventory[i]filters[j]["key"] != filters[j]["val"]:
                            break
                    elif filters[j]["type"] == ">=":
                        if self.__inventory[i]filters[j]["key"] < filters[j]["val"]:
                            break
                    elif filters[j]["type"] == "=<":
                        if self.__inventory[i]filters[j]["key"] > filters[j]["val"]:
                            break
                else:
                    result.append(self.__inventory[i])
                    result_pos.append(i)
            except:        
                pass
        if pos:
            return result_pos
        else:
            return result
    
    def add_items(self, items):
        for i in range(items):
            item_pos = self.return_items(self.item_to_filter(items[i], ["count"]),True)
            if len(item_pos) == 0:
                self.__inventory.append(items[i])
            else:
                pos = item_pos[0]
                self.__inventory[pos]["count"]+=items[i]["count"]
            
    def delete_items(self, items):
        for i in range(items):
            item_pos = self.return_items(self.item_to_filter(items[i], ["count"]),True)
            if not (len(item_pos) == 0):
                pos = item_pos[0]
                self.__inventory[pos]["count"]-=items[i]["count"]
                if self.__inventory[pos]["count"] <= 0:
                    self.__inventory.pop(pos)
                    
    def is_enought_items(self, items):
        for i in range(len(items)):
            item_pos = self.return_items(self.item_to_filter(items[i], ["count"]),True)
            if self.__inventory[pos]["count"] < items[i]["count"]:
                return False
        return True
            
    def heal(self, value):
        self.__hp+=value
        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp
    
    def damage(self, value):
        self.__hp-=value
        if self.__hp < 0:
            self.__hp = 0
            
    def change_max_hp(self, perc):
        self.__max_hp = ceil(self.__max_hp*(1+perc))
        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp
            
    def use_luck(self, chance, info):
        if info["type"] == "positive":
            return chance-chance*(self.stats["lck"]/60)  
        if info["type"] == "negative":
            return chance+(1-chance)*(self.stats["lck"]/60) 