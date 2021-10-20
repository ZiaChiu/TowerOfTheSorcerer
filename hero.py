"""
Author : ZIYE ZHAO
EMAIL: admin@crazyziye.xyz
Website： www.crazyziye.top
license：GPL
Created DATE: 14/10/21 4:29 pm
"""


class Hero:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.blood = 1000
        self.defend = 10
        self.attack = 10
        self.gold = 0
        self.exp = 0
        self.image = ''
        self.x = 0.0
        self.y = 0.0

    def setCoordinate(self, x, y):
        """ set hero's coordinate. """
        self.x = x
        self.y = y

    def addBlood(self, blood):
        """ add hero's blood when hero get blood bottle """
        self.blood += blood

    def minusBlood(self, blood):
        """ minus hero's blood when hero attack monsters or get any events. """
        self.blood -= blood

    def getBlood(self):
        """ get hero's blood volume."""
        return self.blood

    def addAttack(self, attack):
        """ add attack when hero get rubys."""
        self.attack += attack

    def getAttack(self, attack):
        """ get hero's attack value. """
        self.attack -= attack

    def addDefend(self, defend):
        """ add defend when hero get sapphires."""
        self.defend += defend

    def getDefend(self):
        """ get hero's defend value. """
        return self.defend

    def addGold(self, gold):
        """ add hero's money when killed a monster or get any event. """
        self.gold += gold

    def minusGold(self, gold):
        """ minus hero's money when hero go shopping at NPC."""
        self.gold -= gold

    def getGold(self):
        """ get hero's gold volume."""
        return self.gold

    def addExp(self, exp):
        """ add hero's experience when killed a monster or get any event. """
        self.exp += exp

    def minusExp(self, exp):
        """ minus hero's experience when hero go shopping at NPC."""
        self.exp -= exp

    def getExp(self):
        """ get hero's experience volume."""
        return self.exp

    def addLevel(self):
        """ add hero's level when  hero go shopping at NPC or get any event. """
        self.level += 1

    def getLevel(self):
        """ get hero's level."""
        return self.level

    def setImage(self, path: str):
        """ change hero's image when hero moving."""
        self.image = path

    def getImage(self):
        """ Get the current state of the hero."""
        return self.image
