from decimal import Decimal


class Account:
    user_account_id: int
    balance: Decimal

    def __init__(self, user_account_id: int):
        self.user_account_id = user_account_id
        self.balance = Decimal(0)

    def get_user_account_id(self):
        return self.user_account_id

    def get_balance(self):
        return self.balance

    def set_balance(self, value):
        if value >= 0:
            self.balance = value
        else:
            raise ValueError('Баланс должен быть не менее 0 рублей.')

    def refill_balance(self, value: Decimal):
        if value > 0:
            self.balance += value
        else:
            raise ValueError('Сумма пополнения должна быть не менее 0 рублей.')

    def __str__(self):
        return f'account ID: {self.user_account_id}, balance: {self.balance}'
