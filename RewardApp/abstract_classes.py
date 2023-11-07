from abc import ABC, abstractmethod


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass
