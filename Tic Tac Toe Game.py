import pygame
from pygame.locals import *
import random

# Цвета
RED_X = (240, 84, 84)
BLUE_BG = (34, 40, 49)
WHITE_O = (232, 232, 232)
DARK_BLUE_L = (48, 71, 94)

# Размеры экрана
WIDTH = 600
HEIGHT = 720

# Размеры ячеек
CELL_WIDTH = 200
CELL_HEIGHT = 200

class Lattice:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

    def draw(self):
        pygame.draw.line(self.parent_screen, DARK_BLUE_L,  [0, 515], [600, 515], 5)
        pygame.draw.line(self.parent_screen, DARK_BLUE_L, [0, 310], [600, 310], 5)

        pygame.draw.line(self.parent_screen, DARK_BLUE_L, [200, 110], [200, 720], 5)
        pygame.draw.line(self.parent_screen, DARK_BLUE_L, [405, 110], [405, 720], 5)

class X_player:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

    def draw_x(self):
        pygame.draw.line(self.parent_screen, RED_X,  [30, 140], [170, 280], 5 )
        pygame.draw.line(self.parent_screen, RED_X, [30, 280], [170, 140], 5)


class O_player:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

    def draw_o(self):
        pygame.draw.circle(self.parent_screen, WHITE_O, (305,210), 70, 5)

class MainGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        title = pygame.display.set_caption("Tic Tac Toe")
        self.screen.fill(BLUE_BG)

        self.x_player = X_player(self.screen)
        self.x_player.draw_x()

        self.o_player = O_player(self.screen)
        self.o_player.draw_o()

        self.lattice = Lattice(self.screen)
        self.lattice.draw()

        font = pygame.font.SysFont("robotho", 40)
        score = font.render("SCORE", True, WHITE_O)
        self.screen.blit(score, (250, 10))

        pygame.display.flip() # не трогать!

    #def display_score(self):
        #font = pygame.font.SysFont("robotho", 50)
        #score = font.render("SCORE",True, WHITE_O)
        #self.screen.blit(score, (250, 10))
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False


if __name__ == '__main__':
    Game = MainGame()
    Game.run()