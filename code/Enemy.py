from code.Const import WIN_HEIGHT
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += 5
        if self.rect.top >= WIN_HEIGHT:
            self.rect.top = - WIN_HEIGHT