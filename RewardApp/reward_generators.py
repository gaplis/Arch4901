from RewardApp.abstract_classes import ItemFabric
from RewardApp.reward_classes import Gem, Gold, Silver, Copper, Diamond, Ruby, Pearl


class GoldGenerator(ItemFabric):
    rarity = 3

    def create_item(self):
        return Gold()


class GemGenerator(ItemFabric):
    rarity = 1

    def create_item(self):
        return Gem()


class SilverGenerator(ItemFabric):
    rarity = 10

    def create_item(self):
        return Silver()


class CopperGenerator(ItemFabric):
    rarity = 10

    def create_item(self):
        return Copper()


class DiamondGenerator(ItemFabric):
    rarity = 10

    def create_item(self):
        return Diamond()


class PearlGenerator(ItemFabric):
    rarity = 10

    def create_item(self):
        return Pearl()


class RubyGenerator(ItemFabric):
    rarity = 10

    def create_item(self):
        return Ruby()
