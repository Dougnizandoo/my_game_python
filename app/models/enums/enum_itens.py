from enum import Enum


class EnumWeapon(Enum):
    SWORD = 1
    DAGGER = 2
    STAFF = 3

class EnumArmor(Enum):
    HOOD = 1
    ARMOR = 2
    TUNIC = 3

class EnumConsumables(Enum):
    POTION = 1
    FOOD = 2

class EnumStatus(Enum):
    HP = 1
    ATTACK = 2
    DEFENSE = 3
