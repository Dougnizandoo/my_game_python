from dataclasses import dataclass, field
from app.models.enums import EnumStatus


@dataclass
class ArmorStats:
    defense: int = 0
    status_to_upgrade: dict[EnumStatus, int] = field(
        default_factory=lambda: {EnumStatus.HP: 0}
    )


@dataclass
class WeaponStats:
    attack: int = 0
    heal: int = 0


# explain what the consumable gonna boost
@dataclass
class StatusBoost:
    modifiers: dict[EnumStatus, int] = field(default_factory=lambda: {EnumStatus.HP: 3})
