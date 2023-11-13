# 2) Переписать код SpeedCalculation в соответствии с Open-Closed Principle:
# Подсказка: создайте два дополнительных класса Car и Bus(наследников Vehicle),
# напишите метод calculateAllowedSpeed().
# Использование этого метода позволит сделать класс SpeedCalculation соответствующим OCP

class Vehicle:
    max_speed: float

    def __init__(self, max_speed: float):
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed


class Car(Vehicle):
    def __init__(self, max_speed: float, type_car: str):
        super().__init__(max_speed)
        self.type_car = type_car


class Bus(Vehicle):
    def __init__(self, max_speed: float, type_bus: str, number_of_seats: int):
        super().__init__(max_speed)
        self.type_bus = type_bus
        self.number_of_seats = number_of_seats


class SpeedCalculation:
    @staticmethod
    def calculate_allowed_speed(vehicle: Bus | Car):
        if isinstance(vehicle, Car):
            return vehicle.get_max_speed() * 0.8
        elif isinstance(vehicle, Bus):
            return vehicle.get_max_speed() * 0.6
        return 0.0
