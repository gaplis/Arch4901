from typing import List

from MVCApp.Model.Domain.student import Student
from MVCApp.Controller.interfaces.i_get_controller import IGetController
from MVCApp.Controller.interfaces.i_get_view import IGetView
from MVCApp.Controller.interfaces.i_get_model import IGetModel


class Controller(IGetController):
    def __init__(self, model: IGetModel, view: IGetView):
        self.model = model
        self.view = view
        self.students = []

    def test(self, studs: List[Student]) -> bool:
        if len(studs) > 0:
            return True
        else:
            return False

    def update(self):
        # MVP
        self.students = self.model.get_all_students()

        if self.test(self.students):
            self.view.print_all_students(self.students)
        else:
            print("Модель недоступна!")

        # MVC
        # Логика контроллера
        # self.view.print_all_students(self.model.get_all_students())
