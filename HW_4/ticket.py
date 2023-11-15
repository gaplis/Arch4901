from datetime import datetime, timedelta
from decimal import Decimal
from random import randint


class Ticket:
    id_: int
    departure_zone: int
    arrival_zone: int
    route_number: int
    departure_time: datetime
    arrival_time: datetime
    buyer_id: int
    is_used: bool
    price: Decimal
    place: str

    def __init__(self, buyer_id, is_used):
        self.id_ = randint(1, 10000)
        self.departure_zone = randint(1, 10000)
        self.arrival_zone = randint(1, 10000)
        self.route_number = randint(1, 10000)
        self.departure_time = datetime.now()
        self.arrival_time = self.departure_time + timedelta(hours=1)
        self.buyer_id = buyer_id
        self.is_used = is_used
        self.price = Decimal(randint(60, 100)) + round(Decimal(0.99), 2)
        self.place = 'random_str'

    def get_id(self):
        return self.id_

    def get_departure_zone(self):
        return self.departure_zone

    def get_arrival_zone(self):
        return self.arrival_zone

    def get_route_number(self):
        return self.route_number

    def get_departure_time(self):
        return self.departure_time

    def get_arrival_time(self):
        return self.arrival_time

    def get_buyer_id(self):
        return self.buyer_id

    def get_is_used(self):
        return self.is_used

    def get_price(self):
        return self.price

    def get_place(self):
        return self.place

    def set_is_used(self):
        self.is_used = not self.is_used

    def set_price(self, value: Decimal):
        self.price = value

    def __str__(self):
        return f'ticket ID: {self.id_}, departure zone: {self.departure_zone}, arrival zone: {self.arrival_zone}, ' \
               f'departure time: {self.departure_time}, arrival time: {self.arrival_time}, ' \
               f'route number: {self.route_number}, buyer ID: {self.buyer_id}, is used: {self.is_used}, ' \
               f'price: {self.price}, place: {self.place}'
