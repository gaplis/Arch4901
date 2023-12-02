from abc import ABC, abstractmethod


class IGetController(ABC):

    @abstractmethod
    def update(self):
        pass
