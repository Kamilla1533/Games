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

class User:
    def __init__(self, parent_screen, image):
        self.parent_screen = parent_screen
        self.image = image

    def set_parent_screen(self, parent_screen):
        self.parent_screen = parent_screen

    def get_parent_screen(self):
       return self.parent_screen

    def set_image(self, image):
        self.image = image

    def get_image(self):
        return self.image

    def draw_x(self, pos_x, pos_y):
        self.parent_screen.blit(self.image, (pos_x, pos_y))
        pygame.display.flip()

class MainGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        title = pygame.display.set_caption("Tic Tac Toe")
        self.screen.fill(BLUE_BG)

        image_X = pygame.image.load("assets/x_player.png").convert()
        self.x_player = User(self.screen, image_X)

        image_O = pygame.image.load("assets/o_player.png").convert()
        self.o_player = User(self.screen, image_O)

        font = pygame.font.SysFont("robotho", 50)
        score = font.render("SCORE", True, WHITE_O)
        self.screen.blit(score, (250, 10))

        pygame.display.flip() # не трогать!


    def turn_of_the_move(self):
        pass

    def draw_lattice(self):
        pygame.draw.rect(self.screen, LIGHT_BLUE_L, (0, 515, 610, 5))
        pygame.draw.rect(self.screen, LIGHT_BLUE_L, (0, 310, 610, 5))
        pygame.draw.rect(self.screen, LIGHT_BLUE_L, (200, 110, 5, 610))
        pygame.draw.rect(self.screen, LIGHT_BLUE_L, (405, 110, 5, 610))
        pygame.display.flip()

    def start_game(self):
        self.draw_lattice()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    # управление
                    elif event.key == K_KP1:
                        self.x_player.draw_x(L_1[0], L_1[1])

                    elif event.key == K_KP2:
                        self.o_player.draw_x(L_2[0], L_2[1])

                    elif event.key == K_KP3:
                        self.x_player.draw_x(L_3[0], L_3[1])

                    elif event.key == K_KP4:
                        self.x_player.draw_x(L_4[0], L_4[1])

                    elif event.key == K_KP5:
                        self.x_player.draw_x(L_5[0], L_5[1])

                    elif event.key == K_KP6:
                        self.o_player.draw_x(L_6[0], L_6[1])

                    elif event.key == K_KP7:
                        self.x_player.draw_x(L_7[0], L_7[1])

                    elif event.key == K_KP8:
                        self.x_player.draw_x(L_8[0], L_8[1])

                    elif event.key == K_KP9:
                        self.x_player.draw_x(L_9[0], L_9[1])

                elif event.type == QUIT:
                    running = False

            self.start_game()

if __name__ == '__main__':
    Game = MainGame()
    Game.run()
