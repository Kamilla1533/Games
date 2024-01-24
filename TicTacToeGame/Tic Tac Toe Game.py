import pygame
from pygame.locals import *

# Цвета
RED_X = (240, 84, 84)
BLUE_BG = (34, 40, 49)
WHITE_O = (232, 232, 232)
LIGHT_BLUE_L = (48, 71, 94)

# Размеры экрана
WIDTH = 600
HEIGHT = 720

# Размеры ячеек
CELL_WIDTH = 200
CELL_HEIGHT = 200

# Раскладка клавы
L_1 = [0, 520]
L_2 = [205, 520]
L_3 = [410, 520]
L_4 = [0, 315]
L_5 = [205, 315]
L_6 = [410, 315]
L_7 = [0, 110]
L_8 = [205, 110]
L_9 = [410, 110]

class Lattice:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

    def draw(self):
        pygame.draw.rect(self.parent_screen, LIGHT_BLUE_L, (0, 515, 610, 5))
        pygame.draw.rect(self.parent_screen, LIGHT_BLUE_L, (0, 310, 610, 5))

        pygame.draw.rect(self.parent_screen, LIGHT_BLUE_L,(200, 110, 5, 610))
        pygame.draw.rect(self.parent_screen, LIGHT_BLUE_L, (405, 110, 5, 610))


class X_player:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x_image = pygame.image.load("assets/x_player.png").convert()

    def draw_x(self, pos_x, pos_y):
        self.parent_screen.blit(self.x_image, (pos_x, pos_y))
        pygame.display.flip()


class O_player:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.o_image = pygame.image.load("assets/o_player.png")

    def draw_o(self):
        self.parent_screen.blit(self.o_image, (205, 110))
        pygame.display.flip()
        pygame.draw.circle(self.parent_screen, WHITE_O, (305,210), 70, 5)

class MainGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        title = pygame.display.set_caption("Tic Tac Toe")
        self.screen.fill(BLUE_BG)
        self.x_player = X_player(self.screen)
        #self.o_player = O_player(self.screen)
        self.lattice = Lattice(self.screen)
        self.lattice.draw()

        font = pygame.font.SysFont("robotho", 50)
        score = font.render("SCORE", True, WHITE_O)
        self.screen.blit(score, (250, 10))

        pygame.display.flip() # не трогать!



    def start_game(self):
        pass


    def turn_of_the_move(self):
        pass


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    # раскладка клавы
                    elif event.key == K_KP1:
                        self.x_player.draw_x(L_1[0], L_1[1])

                    elif event.key == K_KP2:
                        self.x_player.draw_x(L_2[0], L_2[1])

                    elif event.key == K_KP3:
                        self.x_player.draw_x(L_3[0], L_3[1])

                    elif event.key == K_KP4:
                        self.x_player.draw_x(L_4[0], L_4[1])

                elif event.type == QUIT:
                    running = False
            self.start_game()

if __name__ == '__main__':
    Game = MainGame()
    Game.run()
