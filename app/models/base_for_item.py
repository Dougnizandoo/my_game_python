from abc import ABC


class BaseForItem(ABC):
    def __init__(self, name: str = None, description: str = None):
        self.__name = name or "Unknwon"
        self.__description = description or "Unknwon"
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def description(self) -> str:
        return self.__description
