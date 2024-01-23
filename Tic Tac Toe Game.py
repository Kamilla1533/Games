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

class Lattice:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.board = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]

        self.graph_board = [[[None, None], [None, None], [None, None]],
                            [[None, None], [None, None], [None, None]],
                            [[None, None],[None, None], [None, None]]]

    def draw(self):
        pygame.draw.rect(self.parent_screen, LIGHT_BLUE_L, (0, 515, 610, 5))
        pygame.draw.rect(self.parent_screen, LIGHT_BLUE_L, (0, 310, 610, 5))

        pygame.draw.rect(self.parent_screen, LIGHT_BLUE_L,(200, 110, 5, 610))
        pygame.draw.rect(self.parent_screen, LIGHT_BLUE_L, (405, 110, 5, 610))


class X_player:
    def __init__(self, parent_screen):
        #self.pos_x = pos_x
        #self.pos_y = pos_y
        self.parent_screen = parent_screen
        self.x_image = pygame.image.load("x_player.png").convert()


class O_player:
    def __init__(self, parent_screen):
        #self.pos_x = pos_x
        #self.pos_y = pos_y
        self.parent_screen = parent_screen
        self.o_image = pygame.image.load("o_player.png").convert()

    def draw_o(self):
        self.parent_screen.blit(self.o_image, (None, None))
        pygame.display.flip()


class MainGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        title = pygame.display.set_caption("Tic Tac Toe Game")
        self.screen.fill(BLUE_BG)

        self.x_player = X_player(self.screen)

        self.o_player = O_player(self.screen)

        self.lattice = Lattice(self.screen)
        self.lattice.draw()

        font = pygame.font.SysFont("robotho", 45)
        score = font.render("SCORE", True, WHITE_O)
        self.screen.blit(score, (250, 10))

        pygame.display.flip() # не трогать!

    #def display_score(self):
        #font = pygame.font.SysFont("robotho", 50)
        #score = font.render("SCORE",True, WHITE_O)
        #self.screen.blit(score, (250, 10))

    def draw_lat(self):
        for i in range(3):
            for j in range(3):
                if self.lattice.board[i][j] == "X":
                    self.lattice.graph_board[i][j][0] = self.x_player.x_image
                    self.lattice.graph_board[i][j][1] = self.x_player.x_image.get_rect(center =(j*300+150, i*300+150))
                elif self.lattice.board[i][j] == "O":
                    self.lattice.graph_board[i][j][0] = self.o_player.o_image
                    self.lattice.graph_board[i][j][1] = self.o_player.o_image.get_rect(center=(j * 300 + 150, i * 300 + 150))

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
