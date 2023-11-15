from random import randint
from decimal import Decimal

from HW_4.account import Account
from HW_4.ticket import Ticket


class User:
    id_: int
    name: str
    tickets: list[Ticket]
    login: str
    password_hash_code: str
    account: Account

    def __init__(self, name, login, password_hash_code):
        self.id_ = randint(1, 10000)  # И это я тоже по простому пока написал)
        self.name = name
        self.tickets = []
        self.login = login
        self.password_hash_code = password_hash_code
        self.account = Account(self.id_)

    def get_id(self):
        return self.id_

    def get_name(self):
        return self.name

    def get_tickets(self):
        return self.tickets

    def get_login(self):
        return self.login

    def get_password_hash_code(self):
        return self.password_hash_code

    def get_account(self):
        return self.account.user_account_id

    def set_name(self, value: str):
        self.name = value

    # Этот метод я написал как пример, разумеется шифрование будет куда сложнее)
    def set_password(self, value: str):
        new_password = hash(value)
        self.password_hash_code = str(new_password)

    def buy_ticket(self):
        new_ticket = Ticket(self.id_, True)
        if new_ticket.get_price() > self.account.get_balance():
            raise ValueError(f'На балансе недостаточно средств: '
                             f'билет стоит {new_ticket.get_price()}, на счёте {self.account.get_balance()}')
        self.account.set_balance(self.account.get_balance() - new_ticket.get_price())
        self.tickets.append(new_ticket)

    def __str__(self):
        info = f'ID: {self.id_} \n' \
               f'Name: {self.name} \n' \
               f'Login: {self.login} \n' \
               f'Crypto Password: {self.password_hash_code} \n' \
               f'Account: {self.account} \n' \
               f'Tickets: '
        for ticket in self.tickets:
            info += f'{ticket}'
        return info


if __name__ == '__main__':
    user = User('Илья', 'gaplis', '1q2w3e4r')
    print(user)
    print()
    user.account.refill_balance(Decimal(120))
    print(user)
    print()
    user.buy_ticket()
    print(user)
    print()
    user.buy_ticket()
