from abc import ABC, abstractmethod


class IGetModel(ABC):

    @abstractmethod
    def get_all_students(self):
        pass
