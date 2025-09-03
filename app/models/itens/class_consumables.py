from app.models.itens.base_for_item import BaseForItem
from app.models.enums import EnumConsumables, EnumClasses
from app.models.dataclasses import StatusBoost


class Consumable(BaseForItem):
    def __init__(self, chosen_item: EnumConsumables = None, 
                 allowed_classes: list[EnumClasses] = None, 
                 consumable_effects: StatusBoost = None):
        self._chosen_item = chosen_item or EnumConsumables.POTION
        name = chosen_item.name if chosen_item else EnumConsumables.POTION.name
        super().__init__(name, allowed_classes)
        self._effects = consumable_effects or StatusBoost()

    @property
    def effects(self) -> StatusBoost:
        return self._effects
    
    @property
    def description(self) -> str:
        parts = [f"{status.name}: {value}" for status, value in self.effects.modifiers.items()]
        return f"This item will raise: {', '.join(parts)}"
