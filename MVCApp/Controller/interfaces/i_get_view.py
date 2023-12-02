from abc import ABC, abstractmethod
from typing import List

from MVCApp.Model.Domain.student import Student
from MVCApp.Controller.interfaces.i_get_controller import IGetController


class IGetView(ABC):

    @abstractmethod
    def print_all_students(self, students: List[Student]):
        pass

    @abstractmethod
    def set_controller(self, control: IGetController):
        pass
