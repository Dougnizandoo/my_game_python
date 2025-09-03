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
