import pygame
from pygame.locals import *
import time
import random


class Apple:
    def __init__(self, parent_screen, red_color, pos_x, pos_y):
        self.sizeApple = 30
        self.red = red_color
        self.parent_screen = parent_screen
        self.apple_pos_x = random.randrange(0, pos_x - self.sizeApple, self.sizeApple)
        self.apple_pos_y = random.randrange(0, pos_y - self.sizeApple, self.sizeApple)

    def draw_random_apple(self):
        pygame.draw.rect(self.parent_screen, self.red,
                         (self.apple_pos_x, self.apple_pos_y, self.sizeApple, self.sizeApple))


class Snake:
    def __init__(self, parent_screen, black_color, green_color, pos_x, pos_y, white_color):
        self.width = pos_x
        self.height = pos_y
        self.black = black_color
        self.green = green_color
        self.white = white_color
        self.parent_screen = parent_screen
        self.snake_size = 30
        # self.snake_speed = 10
        self.snake_pos_x = (pos_x / 2) - self.snake_size
        self.snake_pos_y = (pos_y / 2) - self.snake_size
        self.direction = None

    def draw(self):
        pygame.draw.rect(self.parent_screen, self.black,
                         (self.snake_pos_x - 1, self.snake_pos_y - 1, self.snake_size + 2, self.snake_size + 2))
        pygame.draw.rect(self.parent_screen, self.green,
                         (self.snake_pos_x, self.snake_pos_y, self.snake_size, self.snake_size))

    def left_move(self):
        self.direction = "left"

    def right_move(self):
        self.direction = "right"

    def up_move(self):
        self.direction = "up"

    def down_move(self):
        self.direction = "down"

    def walk(self):
        if self.direction == "left":
            self.snake_pos_x -= self.snake_size
            if self.snake_pos_x < -self.snake_size:
                self.snake_pos_x = self.width

        elif self.direction == "right":
            self.snake_pos_x += self.snake_size
            if self.snake_pos_x > self.width:
                self.snake_pos_x = 0

        elif self.direction == "up":
            self.snake_pos_y -= self.snake_size
            if self.snake_pos_y < -self.snake_size:
                self.snake_pos_y = self.height

        elif self.direction == "down":
            self.snake_pos_y += self.snake_size
            if self.snake_pos_y > self.height:
                self.snake_pos_y = 0

        self.parent_screen.fill(self.black)
        self.draw()


class MainGame:
    def __init__(self):
        # запуск игры
        pygame.init()

        # размер окна
        self.SC_WIDTH = 720
        self.SC_HEIGHT = 720

        # Цвета
        self.black = (51, 44, 57)
        self.green = (96, 158, 162)
        self.red = (201, 44, 109)
        self.white = (240, 238, 237)

        self.screen = pygame.display.set_mode((self.SC_WIDTH, self.SC_HEIGHT))
        title = pygame.display.set_caption("Snake")
        self.screen.fill(self.black)

        self.snake = Snake(self.screen, self.black, self.green, self.SC_WIDTH, self.SC_HEIGHT, self.white)
        self.snake.draw()

        self.apple = Apple(self.screen, self.red, self.SC_WIDTH, self.SC_HEIGHT)
        self.apple.draw_random_apple()

    def start_game(self):
        self.snake.walk()
        self.apple.draw_random_apple()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.up_move()
                    elif event.key == K_DOWN:
                        self.snake.down_move()
                    elif event.key == K_LEFT:
                        self.snake.left_move()
                    elif event.key == K_RIGHT:
                        self.snake.right_move()

                elif event.type == QUIT:
                    running = False

            self.start_game()

            time.sleep(0.15)
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    Game = MainGame()
    Game.run()
