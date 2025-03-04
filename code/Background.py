import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self):
        self.rect.centery += 1
        if self.rect.top >= WIN_HEIGHT:
            self.rect.top = - WIN_HEIGHT
