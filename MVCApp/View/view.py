from typing import List
from MVCApp.Controller.interfaces.i_get_controller import IGetController
from MVCApp.Controller.interfaces.i_get_view import IGetView
from MVCApp.Model.Domain.student import Student


class View(IGetView):
    def __init__(self):
        self.control = None

    def set_controller(self, control: IGetController):
        self.control = control

    def call_model(self):
        self.control.update()

    def print_all_students(self, students: List[Student]):
        print("------------ Список студентов ------------")
        for s in students:
            print(s)

