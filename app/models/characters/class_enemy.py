from app.models.characters.base_for_char import BaseForChar
from app.models.enums import EnumEnemy
from typing import Optional
from app.models.dataclasses import CharStatus, Inventory
from app.models.classes import BaseForClass


_default_status_values = {
    EnumEnemy.SLIME: CharStatus(hp=10, attack=1, defense=1),
    EnumEnemy.GOBLIN: CharStatus(hp=15, attack=3, defense=1),
    EnumEnemy.ZOMBIE: CharStatus(hp=17, attack=4, defense=2)
}

class Enemy(BaseForChar):
    def __init__(self, 
                 enemy_type: Optional[EnumEnemy] = None, level: int = 1,
                 enemy_hp: int = None, enemy_attack: int = None, enemy_defense: int = None, 
                 enemy_class: Optional[BaseForClass] = None, inventory: Optional[Inventory] = None
                 ):
        self._enemy_type = enemy_type or EnumEnemy.GOBLIN

        name = self._enemy_type.name 
        current_class = enemy_class
        hp = enemy_hp or _default_status_values[self.enemy_type].hp
        attack = enemy_attack or _default_status_values[self.enemy_type].attack
        defense = enemy_defense or _default_status_values[self.enemy_type].defense

        super().__init__(name, level, hp, attack, defense, current_class=current_class, inventory=inventory)

    @property
    def enemy_type(self):
        return self._enemy_type
