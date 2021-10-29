"""
Author : ZIYE ZHAO
EMAIL: admin@crazyziye.xyz
Website： www.crazyziye.top
license：GPL
Created DATE: 22/10/21 3:21 pm
"""


import database
from game import *


class Monster(GameObject):
    def __init__(self, name, data: database.Data, game):
        super(Monster, self).__init__(game=game, height=32, width=32, position=Vector2D(self.get_x()))
        self.db = data
        self.name = name

    def get_data(self, ID):
        dataList = [self.__get_name(ID),
                    self.__get_X(ID),
                    self.__get_Y(ID),
                    self.__get_attack(ID),
                    self.__get_defend(ID),
                    self.__get_blood(ID),
                    self.__get_exp(ID),
                    self.__get_gold(ID),
                    self.__get_Image(ID)]
        return dataList

    def __get_X(self, ID):
        x = self.db.get_row('x', 'monsterView', 'monsterID', ID)
        return x

    def __get_Y(self, ID):
        y = self.db.get_row('y', 'monsterView', 'monsterID', ID)
        return y

    def __get_name(self, ID):
        name = self.db.get_row('MonsterName', 'monsterView', 'monsterID', ID)
        return name

    def __get_attack(self, ID):
        attack = self.db.get_row('attack', 'monsterView', 'monsterID', ID)
        return attack

    def __get_defend(self, ID):
        defend = self.db.get_row('defend', 'monsterView', 'monsterID', ID)
        return defend

    def __get_blood(self, ID):
        blood = self.db.get_row('blood', 'monsterView', 'monsterID', ID)
        return blood

    def __get_gold(self, ID):
        gold = self.db.get_row('gold', 'monsterView', 'monsterID', ID)
        return gold

    def __get_exp(self, ID):
        exp = self.db.get_row('exp', 'monsterView', 'monsterID', ID)
        return exp

    def __get_Image(self, ID):
        image = self.db.get_row('ImagePath', 'monsterView', 'monsterID', ID)
        return image

    def update(self, seconds):
        pass
