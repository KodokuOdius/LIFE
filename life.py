# Source:
# https://dementiy.github.io/assignments/life/

# Rules
# Место действия этой игры — «вселенная» — это размеченная на клетки поверхность или плоскость 
# — безграничная, ограниченная, или замкнутая (в пределе — бесконечная плоскость).

# Каждая клетка на этой поверхности может находиться в двух состояниях: 
# быть «живой» (заполненной) или быть «мёртвой» (пустой). Клетка имеет восемь соседей, окружающих её.

# Распределение живых клеток в начале игры называется первым поколением. 
# Каждое следующее поколение рассчитывается на основе предыдущего по таким правилам:
#   в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;
#   если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить; 
#   в противном случае, если соседей меньше двух или больше трёх, клетка умирает («от одиночества» или «от перенаселённости»)

# Игра прекращается, если
# на поле не останется ни одной «живой» клетки
# конфигурация на очередном шаге в точности (без сдвигов и поворотов) 
# повторит себя же на одном из более ранних шагов (складывается периодическая конфигурация)
# при очередном шаге ни одна из клеток не меняет своего состояния 
# (складывается стабильная конфигурация; предыдущее правило, вырожденное до одного шага назад)

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
        self.width = width
        self.height = height
        self.speed = speed

        self.window = []
        for _ in range(height):
            _temp = []
            for __ in range(width):
                _temp.append(0)

            self.window.append(_temp)


    def first_generate(self):
        from random import sample as s

        first_cells = self.width * self.height * 0.1

        popl = [
            (i, j) 
            for i in range(self.height) 
                for j in range(self.width)
        ]

        for x, y in s(popl, int(first_cells)):
            self.window[x][y] = 1



    def show(self):
        for i in range(self.height):
            for j in range(self.width):
                el = self.window[i][j]
                print(
                    '\x1b[6;30;42m' + '+' + '\x1b[0m' if el == 1 
                    else '\x1b[6;30;41m' + '-' + '\x1b[0m', 
                    end=''
                )
            print()


    def analys(self):   
        new = self.window

        for i in range(self.height):
            for j in range(self.width):
                total_sum = 0
                if i-1 >= 0:
                    total_sum += sum(self.window[i-1][j-1 if j-1 >= 0 else j: j+2])
        
                total_sum += sum(self.window[i][j-1 if j-1 >= 0 else j : j+2]) - self.window[i][j]

                if i+1 < len(self.window):
                    total_sum += sum(self.window[i+1][j-1 if j-1 >= 0 else j : j+2])
                
                if total_sum == 3 and new[i][j] == 0:
                    new[i][j] = 1
                elif total_sum in [2, 3] and new[i][j] == 1:
                    continue
                else:
                    new[i][j] = 0

                #new[i][j] = 1 if total_sum in [2, 3] else 0

        self.window = new
        



    def start(self, *args, **kwds) -> None:
        self.first_generate()
        run = True

        while run:
            self.show()
            time.sleep(1 / self.speed)

            self.analys()

            # input()

            os.system("cls")


if __name__ == "__main__":
    # game = LIFE(320, 240, 20)
    # game.run()
    print()

    FPS = 120

    life = Universe(100, 45, FPS)

    life.start()

