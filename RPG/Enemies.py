import pygame
import random

cat = pygame.image.load("cat.png")
pboss_sprite = pygame.image.load("Inis character.jpg")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite = None
        self.health = None
        self.attacks = None  # 2 dimensional array with lists for attack damage, description, and chance of success respectively
        self.speed = None
        self.attacknum = None
        self.battleimg_pos = (100, 100)
        self.xp = None

    def attack(self):
        num = random.randint(0, self.attacknum) - 1
        attack = self.attacks[num]
        chance = attack[2]  # find the chance of success of the given attack
        res = random.randint(0, chance)
        if res == 1:
            desc = "The opponent's attack missed!"
            return [0, desc, False]
        else:
            damage_range = attack[0]
            i = damage_range[0]
            z = damage_range[1]
            damage = random.randint(i, z)
            desc = attack[1]
            return [damage, desc, True]


def minion_make():
    minion = Enemy()
    minion.sprite = cat
    minion.health = 10
    minion.attacks = [[[2, 3], ["The minion slapped you!"], 50]]
    minion.speed = 3
    minion.attacknum = len(minion.attacks)
    minion.xp = 5
    return minion


def purple_boss_make():
    pboss = Enemy()
    pboss.sprite = pboss_sprite
    pboss.health = 10
    pboss.attacks = [[[17, 19], ["The old guy stomped you", "into the ground!"], 50]]
    pboss.speed = 3
    pboss.attacknum = len(pboss.attacks)
    pboss.xp = 20
    return pboss

