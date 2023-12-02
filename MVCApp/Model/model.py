from typing import List
from MVCApp.Model.Domain.student import Student
from MVCApp.Controller.interfaces.i_get_model import IGetModel


class Model(IGetModel):
    def __init__(self, students: List[Student]):
        self.students = students

    def get_all_students(self) -> List[Student]:
        return self.students
