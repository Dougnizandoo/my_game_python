from app.models.classes.base_for_class import BaseForClass
from app.models.dataclasses import SpecialAttack, LevelUpPoints


class Warrior(BaseForClass):
    BASE_POINTS = (1, 2, 3)
    BASE_SPECIAL = (1, 1)

    def __init__(self, current_level: int=1):
        super().__init__(special_attack=SpecialAttack(
                            name="shield-breaker", attack=2, heal=0), 
                         levelup_points=LevelUpPoints(
                            hp=1, attack=1, defense=2), 
                         current_level= current_level)


    def _apply_level_bonus(self):
        self._apply_level_bonus_loop(self.BASE_POINTS, self.BASE_SPECIAL)

    def _apply_level_bonus_loop(self, levelup_points, special_attack):
        super()._apply_level_bonus_loop(levelup_points, special_attack)
        if self.current_level > 3:
            self.special_attack.heal += special_attack[0]
        self.special_attack.attack += special_attack[1]