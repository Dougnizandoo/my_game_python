from dataclasses import dataclass, field
from app.models.itens.base_for_item import BaseForItem
from app.models.classes import EnumClasses
from app.models.itens.enum_itens import EnumArmor, EnumStatus



@dataclass
class ArmorStats:
    defense: int = 0
    status_to_upgrade: dict[EnumStatus, int] = field(
        default_factory=lambda: {EnumStatus.HP: 0}
    )


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
