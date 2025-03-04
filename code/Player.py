from abc import ABC

import pygame.key

from code.Const import WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_UP
from code.Entity import Entity


class Player(Entity, ABC):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= 2
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += 2
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= 3
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 3

        pass

