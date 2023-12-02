class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_age(self) -> int:
        return self.age

    def set_age(self, age: int):
        self.age = age

    def __str__(self) -> str:
        return f"Person [{self.name=}, {self.age=}"
