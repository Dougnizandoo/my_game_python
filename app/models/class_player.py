from app.models.base_for_char import BaseForChar,   Inventory
from app.models.base_for_class import BaseForClass
from typing import Optional


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
        self.char_status.level += 1
