# 1) Переписать код в соответствии с Single Responsibility Principle:
# Подсказка: вынесите метод calculateNetSalary() в отдельный класс

from datetime import date


class Salary:
    def __init__(self, base_salary: float, tax: float):
        self._base_salary = base_salary
        self._tax = tax
        self._clear_salary = self.calculate_net_salary()

    def calculate_net_salary(self):
        count_tax = int(self._base_salary * self._tax)
        return self._base_salary - count_tax

    def get_base_salary(self):
        return self._base_salary

    def set_base_salary(self, new_base_salary: float):
        self._base_salary = new_base_salary
        self._clear_salary = self.calculate_net_salary()

    def get_tax(self):
        return self._tax

    def set_tax(self, new_tax: float):
        self._tax = new_tax
        self._clear_salary = self.calculate_net_salary()

    def get_clear_salary(self):
        return self._clear_salary


class Employee:
    def __init__(self, name: str, dob: date, salary: Salary):
        self.name = name
        self._dob = dob
        self.salary = salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self._dob}"
