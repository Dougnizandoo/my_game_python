from abc import ABC, abstractmethod
from app.models.dataclasses import SpecialAttack, LevelUpPoints


class BaseForClass(ABC):
    def __init__(self, special_attack: SpecialAttack, levelup_points: LevelUpPoints, current_level: int=1):
        self._special_attack = special_attack
        self._levelup_points = levelup_points
        self._current_level = current_level
        if current_level > 1:
            self._apply_level_bonus()
    
    @property
    def class_name(self):
        return self.__class__.__name__

    @property
    def special_attack(self) -> SpecialAttack:
        return self._special_attack

    @property
    def levelup_points(self) -> LevelUpPoints:
        return self._levelup_points
    
    @property
    def current_level(self) -> int:
        return self._current_level
    
    @current_level.setter
    def current_level(self, new_level: int):
        while self.current_level < new_level:
            self._apply_level_bonus()
            self._current_level += 1
    
    @abstractmethod
    def _apply_level_bonus(self):
        pass

    def _apply_level_bonus_loop(self, 
                           levelup_points: tuple[int, int, int], 
                           special_attack: tuple[int, int]):
        self.levelup_points.hp += levelup_points[0]
        self.levelup_points.attack += levelup_points[1]
        self.levelup_points.defense += levelup_points[2]
