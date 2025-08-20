from abc import ABC


class BaseForChar(ABC):
    def __init__(self, name: str, level: int, hp: int, attack: int, defense: int, current_class: object, inventory: dict):
        self.__name = name or "Unknown"
        self.__level = level if level > 0 else 1
        self.__hp = hp if hp > 0 else 1
        self.__attack = attack if attack > 0 else 1
        self.__defense = defense if defense > 0 else 1
        self.__current_class = current_class
        self.__inventory = dict(inventory)
        if "money" not in self.__inventory:
            self.__inventory["money"] = 0
        self.__equipment = {
            "left_hand": None,
            "right_hand": None,
            "armor": None
        }

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if len(value.strip()) > 1:
            self.__name = value.title()
