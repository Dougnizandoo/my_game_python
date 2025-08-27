from abc import ABC


class BaseForItem(ABC):
    def __init__(self, name: str = None):
        self.__name = name or "Unknwon"
    
    @property
    def name(self) -> str:
        return self.__name
