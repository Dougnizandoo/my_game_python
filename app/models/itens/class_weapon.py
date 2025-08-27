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
        super().__init__(name= chosen_weapon.name)
        self._chosen_weapon = chosen_weapon
        self._weapon_stats = weapon_stats or WeaponStats()
        self._who_can_use = allowed_classes or [*EnumClasses]
    
    @property
    def chosen_weapon(self):
        return self._chosen_weapon
    
    @property
    def weapon_stats(self):
        return self._weapon_stats

    @property
    def who_can_use(self):
        return self._who_can_use
    
    def add_allowed_class(self, new_class: EnumClasses):
        if new_class in self.who_can_use:
            raise ValueError(f"{new_class.name} already can use this weapon!")
        self._who_can_use.append(new_class)

    def remove_allowed_class(self, class_to_remove: EnumClasses):
        if class_to_remove not in self.who_can_use:
            raise ValueError(f"{class_to_remove} isn't allowed to use this!")
        self._who_can_use.remove(class_to_remove)
