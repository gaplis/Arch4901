from MVCApp.Model.Domain.person import Person


class Student(Person):
    def __init__(self, name: str, age: int, id_: int):
        super().__init__(name, age)
        self.id_ = id_

    def get_id(self) -> int:
        return self.id_

    def set_id(self, id_: int):
        self.id_ = id_

    def __str__(self) -> str:
        return f"Student  [age={self.get_age()}, name={self.get_name()}, id={self.get_id()}]"
