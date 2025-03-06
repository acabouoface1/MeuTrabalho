import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Estrada':
                list_bg = []
                for i in range(2):  # Bg Fundo images number
                    list_bg.append(Background(f'Estrada{i}', (0, 0)))
                    list_bg.append(Background(f'Estrada{i}', (0, - WIN_HEIGHT)))
                return list_bg
            case 'Player1':
                return Player('Player1', (WIN_WIDTH / 2 - 180,WIN_HEIGHT - 140))
            case 'Player2':
                return Player('Player2', (WIN_WIDTH / 2 + 80,WIN_HEIGHT - 140))
            case 'Enemy1':
                return Enemy('Enemy1', (random.randint(30, WIN_HEIGHT + 30 ), 0 - 400))