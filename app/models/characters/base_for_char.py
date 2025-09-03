from abc import ABC
from typing import Optional
from app.models.classes import BaseForClass
from app.models.dataclasses import Equipment, CharStatus, Inventory


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

    @property
    def decription(self) -> str:
        return f'lv {self.char_status.level}, {self.name} | class: {self.current_class.class_name}'

    # Setters
    @name.setter
    def name(self, value: str):
        if len(value.strip()) > 1:
            self.__name = value.title()
    
    @current_class.setter
    def current_class(self, new_class: BaseForClass):
        self.__current_class = new_class
