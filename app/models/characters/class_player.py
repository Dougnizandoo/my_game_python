from app.models.characters.base_for_char import BaseForChar
from app.models.classes import BaseForClass
from typing import Optional
from app.models.dataclasses import Inventory


class Player(BaseForChar):
    def __init__(self, current_class: BaseForClass = None, name: str = None, 
                 level: int= 1, hp: int= 10, attack: int= 1, defense: int= 2, 
                 inventory: Optional[Inventory] = None):
        super().__init__(name, level, hp, attack, defense, current_class, inventory)
        self.__xp = 0

    @property
    def xp(self) -> int:
        return self.__xp
    
    def gain_xp(self, xp: int):
        self.__xp += xp
        while self.__xp >= self.char_status.level * 10:
            self.__xp -= self.char_status.level * 10
            self._level_up()

    def _level_up(self):
        hp = self.current_class.levelup_points.hp
        attack = self.current_class.levelup_points.attack
        defense = self.current_class.levelup_points.defense
        self.char_status.hp += hp
        self.char_status.attack += attack
        self.char_status.defense += defense
        self.current_class.current_level += 1
        self.char_status.level += 1
