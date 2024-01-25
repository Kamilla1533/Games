import pygame
from pygame.locals import *
import time
import random

SIZE = 30

SC_WIDTH = 720
SC_HEIGHT = 720

BLACK = (51, 44, 57)
GREEN = (96, 158, 162)
RED = (201, 44, 109)
WHITE = (240, 238, 237)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple_pos_x = random.randrange(0, SC_WIDTH - SIZE, SIZE)
        self.apple_pos_y = random.randrange(0, SC_HEIGHT - SIZE, SIZE)

    def draw_random_apple(self):
        pygame.draw.rect(self.parent_screen, RED,(self.apple_pos_x, self.apple_pos_y, SIZE, SIZE))

    def another_spawn(self):
        self.apple_pos_x = random.randrange(0, SC_WIDTH - SIZE, SIZE)
        self.apple_pos_y = random.randrange(0, SC_HEIGHT - SIZE, SIZE)

class Snake:
    def __init__(self, parent_screen,length):
        self.length = length
        self.parent_screen = parent_screen
        self.snake_pos_x = [SIZE] * length
        self.snake_pos_y = [SIZE] * length
        self.direction = None

    def draw(self):
        for i in range(self.length):
            pygame.draw.rect(self.parent_screen, BLACK,(self.snake_pos_x[i] - 1, self.snake_pos_y[i] - 1, SIZE + 2, SIZE + 2))
            pygame.draw.rect(self.parent_screen, GREEN,(self.snake_pos_x[i], self.snake_pos_y[i], SIZE, SIZE))

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
            self.snake_pos_x[0] -= SIZE
            if self.snake_pos_x[0] < 0:
                self.snake_pos_x[0] = SC_WIDTH - SIZE

        elif self.direction == "right":
            self.snake_pos_x[0] += SIZE
            if self.snake_pos_x[0] == SC_WIDTH:
                self.snake_pos_x[0] = 0

        elif self.direction == "up":
            self.snake_pos_y[0] -= SIZE
            if self.snake_pos_y[0] < 0:
                self.snake_pos_y[0] = SC_HEIGHT - SIZE

        elif self.direction == "down":
            self.snake_pos_y[0] += SIZE
            if self.snake_pos_y[0] == SC_HEIGHT:
                self.snake_pos_y[0] = 0

        self.parent_screen.fill(BLACK)
        self.draw()

    def add_length(self):
        self.length +=1
        self.snake_pos_x.append(-1)
        self.snake_pos_y.append(-1)

class MainGame:
    def __init__(self):
        # запуск игры
        pygame.init()
        pygame.mixer.init()
        self.main_song()

        self.screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
        title = pygame.display.set_caption("Snake")
        self.screen.fill(BLACK)

        self.snake = Snake(self.screen, 1)
        self.snake.draw()

        self.apple = Apple(self.screen)
        self.apple.draw_random_apple()

    def reset_score(self):
        self.snake = Snake(self.screen,  1)
        self.apple = Apple(self.screen)

    def collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False

    def main_song(self):
        pygame.mixer.music.load("assets/song.mp3")
        pygame.mixer.music.play()

    def start_game(self):
        self.snake.walk()
        self.apple.draw_random_apple()
        self.display_score()
        pygame.display.flip()

        if self.collision(self.snake.snake_pos_x[0], self.snake.snake_pos_y[0], self.apple.apple_pos_x, self.apple.apple_pos_y):
            biteSound = pygame.mixer.Sound("assets/bite.mp3")
            pygame.mixer.Sound.play(biteSound)
            self.snake.add_length()
            self.apple.another_spawn()

        for i in range(3, self.snake.length):
            if self.collision(self.snake.snake_pos_x[0], self.snake.snake_pos_y[0], self.snake.snake_pos_x[i], self.snake.snake_pos_y[i]):
                endGame = pygame.mixer.Sound("assets/endgame.mp3")
                pygame.mixer.Sound.play(endGame)
                raise "Game over!"

    def display_score(self):
        font = pygame.font.SysFont("robotho", 50)
        score = font.render(f"Score: {self.snake.length}", True, WHITE)
        self.screen.blit(score, (550, 10))

    def game_over_menu(self):
        self.screen.fill(BLACK)
        font = pygame.font.SysFont("robotho", 40)
        game_over = font.render(f"GAME OVER", True, WHITE)
        self.screen.blit(game_over, (250, 300))

        score_show = font.render(f"Your score is {self.snake.length}", True, WHITE)
        self.screen.blit(score_show, (235, 350))

        play_again = font.render("Press Enter to play or Escape to exit", True, WHITE)
        self.screen.blit(play_again, (105, 400))
        pygame.display.flip()
        pygame.mixer.music.stop()

    def run(self):
        running = True
        stop = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        self.main_song()
                        stop = False
                    # snake movement
                    if not stop:
                        if event.key == K_UP and self.snake.direction != "down":
                            self.snake.up_move()
                        elif event.key == K_DOWN and self.snake.direction != "up":
                            self.snake.down_move()
                        elif event.key == K_LEFT and self.snake.direction != "right":
                            self.snake.left_move()
                        elif event.key == K_RIGHT and self.snake.direction != "left":
                            self.snake.right_move()
                elif event.type == QUIT:
                    running = False
            try:
                if not stop:
                    self.start_game()
            except Exception:
                self.game_over_menu()
                stop = True
                self.reset_score()

            time.sleep(0.075)

if __name__ == '__main__':
    Game = MainGame()
    Game.run()
