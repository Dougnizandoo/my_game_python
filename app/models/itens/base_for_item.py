from abc import ABC
from app.models.enums import EnumClasses


class BaseForItem(ABC):
    def __init__(self, name: str = None, allowed_classes: list[EnumClasses] = None):
        self.__name = name or "Unknwon"
        self._who_can_use = allowed_classes or list(EnumClasses)
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def who_can_use(self):
        return self._who_can_use
    
    def add_allowed_class(self, new_class: EnumClasses):
        if new_class in self.who_can_use:
            raise ValueError(f"{new_class.name} already can use this item!")
        self._who_can_use.append(new_class)

    def remove_allowed_class(self, class_to_remove: EnumClasses):
        if class_to_remove not in self.who_can_use:
            raise ValueError(f"{class_to_remove} isn't allowed to use this item!")
        self._who_can_use.remove(class_to_remove)
