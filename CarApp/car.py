from CarApp.abstract_class import Car, FuelStation, ICarWash


class PickUp(Car, FuelStation, ICarWash):
    load_capacity: float

    def __init__(self,
                 brand,
                 model,
                 color,
                 body_type,
                 wheel_count,
                 fuel_type,
                 transmission_type,
                 engine_capacity,
                 load_capacity):
        super().__init__(brand, model, color, body_type, wheel_count, fuel_type, transmission_type, engine_capacity)
        self.load_capacity = load_capacity

    @staticmethod
    def sweep_street():
        print('Подметаем')

    def refill(self):
        print('Заправляемся')

    def weep_windshield(self):
        print('Моем окна')

    def weep_headlights(self):
        print('Моем фары')

    def weep_mirror(self):
        print('Моем зеркала')
