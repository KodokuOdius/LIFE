# Source:
# https://dementiy.github.io/assignments/life/

import pygame
from pygame.locals import *

import os
import time


# Core of Game - Heart of LIFE!
class LIFE():
    def __init__(self, width, height, cell_size) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Set screen size
        self.screen_size = width, height

        # Create new game window
        self.screen = pygame.display.set_mode(self.screen_size)

        # Size of cells
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.speed = 60


    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('white'), (x, 0), (x, self.height))

        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('white'), (0, y), (self.width, y))


    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('black'))

        running = True
        while running:
            for event in pygame.event.get():
                print(event)
                if event.type == QUIT:
                    running = False
                    
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()



class Universe():

    def __init__(self, width, height, speed) -> None:
        self.speed = speed

        self.window = []
        for _ in range(height):
            _temp = []
            for __ in range(width):
                _temp.append(0)

            self.window.append(_temp)


    def show(self):
        for row in self.window:
                print(*row)


    def start(self, *args, **kwds) -> None:
        run = True

        while run:
            self.show()

            time.sleep(1 / self.speed)
            os.system("cls")


if __name__ == "__main__":
    # game = LIFE(320, 240, 20)
    # game.run()
    print()

    FPS = 60

    life = Universe(20, 15, FPS)

    life.start()

