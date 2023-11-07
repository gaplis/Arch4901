from random import randint

from RewardApp.reward_generators import GoldGenerator, GemGenerator, SilverGenerator, CopperGenerator, \
    DiamondGenerator, RubyGenerator, PearlGenerator

REWARDS_LIST = [
    GoldGenerator(),
    GemGenerator(),
    SilverGenerator(),
    CopperGenerator(),
    DiamondGenerator(),
    RubyGenerator(),
    PearlGenerator(),
]

rarity_rewards = [reward for reward in REWARDS_LIST for _ in range(reward.rarity)]

if __name__ == '__main__':
    for i in range(20):
        REWARDS_LIST[randint(0, len(REWARDS_LIST) - 1)].create_item().open()
