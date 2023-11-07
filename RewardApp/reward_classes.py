from RewardApp.abstract_classes import IGameItem


class Gold(IGameItem):
    def open(self):
        print('Gold!')


class Gem(IGameItem):
    def open(self):
        print('Gem!')


class Silver(IGameItem):
    def open(self):
        print('Silver!')


class Copper(IGameItem):
    def open(self):
        print('Copper!')


class Diamond(IGameItem):
    def open(self):
        print('Diamond!')


class Ruby(IGameItem):
    def open(self):
        print('Ruby!')


class Pearl(IGameItem):
    def open(self):
        print('Pearl!')
