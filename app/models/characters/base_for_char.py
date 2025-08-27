from abc import ABC
from dataclasses import dataclass
from typing import Optional
from app.models.itens import BaseForItem
from app.models.classes import BaseForClass


@dataclass
class Equipment:
    left_hand: Optional[BaseForItem] = None
    right_hand: Optional[BaseForItem] = None
    armor: Optional[BaseForItem] = None


@dataclass
class CharStatus:
    level: int = 1
    hp: int = 10
    attack: int = 1
    defense: int = 2


class Inventory():
    def __init__(self, money: int = None, itens: Optional[list[list[BaseForItem]]] = None):
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

    def add_to_inventory(self, item: BaseForItem):
        for group in self.__itens:
            if group[0].name == item.name:
                group.append(item)
                return
        self.__itens.append([item])

    def remove_from_inventory(self, item: BaseForItem):
        for group in self.__itens:
            if group[0].name == item.name:
                if len(group) > 1:
                    group.remove(item)
                else:
                    self.__itens.remove(group)
                return
        raise ValueError(f"You don't have any: '{item.name}'")


# Main classe
class BaseForChar(ABC):
    def __init__(self, name: str, level: int, hp: int, 
                 attack: int, defense: int, current_class: 
                 BaseForClass, inventory: Optional[Inventory] = None):
        self.__name = name or "Unknown"
        self.__char_status = CharStatus(level, hp, attack, defense)
        self.__current_class = current_class
        self.__inventory = inventory or Inventory()
        self.__equipment = Equipment()

    # Getters
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def char_status(self) -> CharStatus:
        return self.__char_status
    
    @property
    def current_class(self) -> object:
        return self.__current_class

    @property
    def inventory(self) -> Inventory:
        return self.__inventory
    
    @property
    def equipment(self) -> Equipment:
        return self.__equipment

    # Setters
    @name.setter
    def name(self, value: str):
        if len(value.strip()) > 1:
            self.__name = value.title()
    
    @current_class.setter
    def current_class(self, new_class: BaseForClass):
        self.__current_class = new_class
