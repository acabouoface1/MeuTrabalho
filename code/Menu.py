import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import C_BLACK, WIN_WIDTH, C_WHITE, MENU_OPTION, C_RED


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/Fundo0.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Som0.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # DRAN IMAGES (Desenhe as imagens)
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(80, "Game", C_BLACK, ((WIN_WIDTH / 2), 60))
            self.menu_text(80, "Car", C_BLACK, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(50, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 50 * i))
                else:
                    self.menu_text(50, MENU_OPTION[i], C_RED, ((WIN_WIDTH / 2), 200 + 50 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True,text_color).convert_alpha()
        text_rect : Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)