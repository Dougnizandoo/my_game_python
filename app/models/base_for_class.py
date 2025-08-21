from abc import ABC
from dataclasses import dataclass


@dataclass
class SpecialAttack:
    name: str
    attack: int = 0
    heal: int = 0


@dataclass
class LevelUpPoints:
    hp: int = 0
    attack: int = 0
    defense: int = 0



class BaseForClass(ABC):
    def __init__(self, special_attack: SpecialAttack, levelup_points: LevelUpPoints):
        self._special_attack = special_attack
        self._levelup_points = levelup_points
    
    @property
    def special_attack(self) -> SpecialAttack:
        return self._special_attack

    @property
    def levelup_points(self) -> LevelUpPoints:
        return self._levelup_points
