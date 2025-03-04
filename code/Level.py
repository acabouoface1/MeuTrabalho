import sys


import pygame
from pygame.display import flip
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window: Surface, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Estrada'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000
        if game_mode in MENU_OPTION[1]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)



    def run(self):
        pygame.mixer_music.load('./asset/Som0.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))

            # Printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidade: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            flip()
            # Collisions
            # EntityMediator.verify_collision(entity_list=self.entity_list)
            # EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida San Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
