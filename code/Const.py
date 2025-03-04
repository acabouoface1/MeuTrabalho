import pygame

# C
C_BLACK =(0, 0, 0)
C_WHITE = (255, 255, 255)
C_RED = (255, 0, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Estrada0': 0,
    'Estrada1': 1,
}


# M
MENU_OPTION = ('New Game 1p',
               'New Game 2p',
                'Score',
                 'Exit'
)

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}

# W
WIN_WIDTH = 688
WIN_HEIGHT = 500

# S
SCORE_POS = {'Title': (WIN_WIDTH/ 2, 50),
             'EnterName': (WIN_WIDTH/ 2, 80),
             'Label': (WIN_WIDTH/ 2, 90),
             'Name': (WIN_WIDTH/ 2, 110),
             0: (WIN_WIDTH/ 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
