import pygame
from pygame.locals import *
import time
import random

SIZE = 30

class Apple:
    def __init__(self, parent_screen, red_color, pos_x, pos_y):
        self.width = pos_x
        self.height = pos_y
        self.sizeApple = 30
        self.red = red_color
        self.parent_screen = parent_screen
        self.apple_pos_x = random.randrange(0, pos_x - self.sizeApple, self.sizeApple)
        self.apple_pos_y = random.randrange(0, pos_y - self.sizeApple, self.sizeApple)

    def draw_random_apple(self):
        pygame.draw.rect(self.parent_screen, self.red,(self.apple_pos_x, self.apple_pos_y, self.sizeApple, self.sizeApple))

    def another_spawn(self):
        self.apple_pos_x = random.randrange(0, self.width - self.sizeApple, self.sizeApple)
        self.apple_pos_y = random.randrange(0, self.height - self.sizeApple, self.sizeApple)


class Snake:
    def __init__(self, parent_screen, black_color, green_color, pos_x, pos_y, white_color, length):
        self.length = length

        self.width = pos_x
        self.height = pos_y
        self.black = black_color
        self.green = green_color
        self.white = white_color
        self.parent_screen = parent_screen
        self.snake_size = 30
        # self.snake_speed = 10
        self.snake_pos_x = [SIZE] * length
        self.snake_pos_y = [SIZE] * length
        self.direction = None

    def draw(self):
        for i in range(self.length):
            pygame.draw.rect(self.parent_screen, self.black,(self.snake_pos_x[i] - 1, self.snake_pos_y[i] - 1, self.snake_size + 2, self.snake_size + 2))
            pygame.draw.rect(self.parent_screen, self.green,(self.snake_pos_x[i], self.snake_pos_y[i], self.snake_size, self.snake_size))

    def left_move(self):
        self.direction = "left"

    def right_move(self):
        self.direction = "right"

    def up_move(self):
        self.direction = "up"

    def down_move(self):
        self.direction = "down"

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.snake_pos_x[i] = self.snake_pos_x[i - 1]
            self.snake_pos_y[i] = self.snake_pos_y[i - 1]


        if self.direction == "left":
            self.snake_pos_x[0] -= self.snake_size
            if self.snake_pos_x[0] < -self.snake_size:
                self.snake_pos_x[0] = self.width

        elif self.direction == "right":
            self.snake_pos_x[0] += self.snake_size
            if self.snake_pos_x[0] > self.width:
                self.snake_pos_x[0] = 0

        elif self.direction == "up":
            self.snake_pos_y[0] -= self.snake_size
            if self.snake_pos_y[0] < -self.snake_size:
                self.snake_pos_y[0] = self.height

        elif self.direction == "down":
            self.snake_pos_y[0] += self.snake_size
            if self.snake_pos_y[0] > self.height:
                self.snake_pos_y[0] = 0

        self.parent_screen.fill(self.black)
        self.draw()

    def add_length(self):
        self.length +=1
        self.snake_pos_x.append(-1)
        self.snake_pos_y.append(-1)


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

        self.snake = Snake(self.screen, self.black, self.green, self.SC_WIDTH, self.SC_HEIGHT, self.white, 1)
        self.snake.draw()

        self.apple = Apple(self.screen, self.red, self.SC_WIDTH, self.SC_HEIGHT)
        self.apple.draw_random_apple()

    def collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False

    def start_game(self):
        self.snake.walk()
        self.apple.draw_random_apple()

        if self.collision(self.snake.snake_pos_x[0], self.snake.snake_pos_y[0], self.apple.apple_pos_x, self.apple.apple_pos_y):
            self.snake.add_length()
            self.apple.another_spawn()

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

            time.sleep(0.09)
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    Game = MainGame()
    Game.run()
