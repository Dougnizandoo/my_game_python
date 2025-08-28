from app.models.itens.base_for_item import BaseForItem
from app.models.itens.enum_itens import EnumWeapon
from app.models.classes import EnumClasses
from dataclasses import dataclass


@dataclass
class WeaponStats:
    attack: int = 0
    heal: int = 0

class Weapon(BaseForItem):
    def __init__(self, 
                 weapon_stats: WeaponStats = None, 
                 chosen_weapon: EnumWeapon = EnumWeapon.SWORD,
                 allowed_classes: list[EnumClasses] = None):
        self._chosen_weapon = chosen_weapon
        self._weapon_stats = weapon_stats or WeaponStats()
        super().__init__(name= chosen_weapon.name, allowed_classes=allowed_classes)

    @property
    def chosen_weapon(self):
        return self._chosen_weapon
    
    @property
    def weapon_stats(self):
        return self._weapon_stats

    @property
    def who_can_use(self):
        return self._who_can_use
