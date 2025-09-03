from app.models.itens.base_for_item import BaseForItem
from app.models.enums import EnumArmor, EnumClasses
from app.models.dataclasses import ArmorStats

class Armor(BaseForItem):
    def __init__(self, armor_chosen: EnumArmor = None, 
                 allowed_classes: list[EnumClasses] = None,
                 armor_stats: ArmorStats = None):
        self._armor_chosen = armor_chosen or EnumArmor.ARMOR
        name = armor_chosen.name if armor_chosen else None
        super().__init__(name, allowed_classes=allowed_classes)
        self._armor_status = armor_stats or ArmorStats(defense=1)
    
    @property
    def armor_stats(self):
        return self._armor_status
