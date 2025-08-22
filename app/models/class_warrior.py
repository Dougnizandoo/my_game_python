from app.models.base_for_class import BaseForClass, LevelUpPoints, SpecialAttack


class Warrior(BaseForClass):
    def __init__(self, current_level: int=1):
        super().__init__(special_attack=SpecialAttack(
                            name="shield-breaker", attack=2, heal=0), 
                         levelup_points=LevelUpPoints(
                            hp=1, attack=1, defense=2), 
                         current_level= current_level)


    def _apply_level_bonus(self):
        levelup_points = (1, 2, 3)
        special_attack = (1, 1)
        self._apply_level_bonus_loop(levelup_points, special_attack)
