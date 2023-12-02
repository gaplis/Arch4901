from typing import List

from MVCApp.Controller.controller import Controller
from MVCApp.Model.Domain.student import Student
from MVCApp.Controller.interfaces.i_get_model import IGetModel
from MVCApp.Controller.interfaces.i_get_view import IGetView
from MVCApp.Controller.interfaces.i_get_controller import IGetController
from MVCApp.Model.model import Model
from MVCApp.View.view import View


def main():
    students: List[Student] = []
    s1 = Student("Сергей", 21, 101)
    s2 = Student("Андрей", 22, 111)
    s3 = Student("Иван", 22, 121)
    s4 = Student("Игорь", 23, 301)
    s5 = Student("Даша", 25, 171)
    s6 = Student("Лена", 23, 104)
    students.append(s1)
    students.append(s2)
    students.append(s3)
    students.append(s4)
    students.append(s5)
    students.append(s6)

    mod: IGetModel = Model(students)
    view: IGetView = View()

    control: IGetController = Controller(mod, view)

    view.set_controller(control)

    control.update()


if __name__ == '__main__':
    main()
