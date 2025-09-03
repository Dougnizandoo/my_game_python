from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.itens import BaseForItem



@dataclass
class Equipment:
    left_hand: Optional["BaseForItem"] = None
    right_hand: Optional["BaseForItem"] = None
    armor: Optional["BaseForItem"] = None


@dataclass
class CharStatus:
    level: int = 1
    hp: int = 10
    attack: int = 1
    defense: int = 2


@dataclass
class Inventory():
    def __init__(self, money: int = None, itens: Optional[list[list["BaseForItem"]]] = None):
        self.__money = money or 0
        self.__itens = itens or []
    
    @property
    def money(self) -> int:
        return self.__money

    def add_money(self, value: int):
        self.__money += value
    
    def remove_money(self, value: int):
        if self.__money - value < 0:
            raise Exception(f"You can't spend this value!\nYou only have {self.money} coins!")
        self.__money -= value

    @property
    def itens(self) -> dict:
        itens = dict()
        for item_group in self.__itens:
            itens[item_group[0].name] = len(item_group)
        return itens

    def add_to_inventory(self, item: "BaseForItem"):
        for group in self.__itens:
            if group[0].name == item.name:
                group.append(item)
                return
        self.__itens.append([item])

    def remove_from_inventory(self, item: "BaseForItem"):
        for group in self.__itens:
            if group[0].name == item.name:
                if len(group) > 1:
                    group.remove(item)
                else:
                    self.__itens.remove(group)
                return
        raise ValueError(f"You don't have any: '{item.name}'")
