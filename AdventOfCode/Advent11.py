
import numpy as np
import time
from intcode_computer import intcode_computer


def initialize():

    with open('paint.txt', 'r') as file:
        a = file.read()

    intcode_str = a.split(",")

    intcode_init = []

    for string in intcode_str:
        intcode_init.append(int(string))

    extra_mem = [0 for _ in range(100000)]

    return intcode_init + extra_mem


computer = intcode_computer(initialize())

finished = False
DY = {0: -1, 1: 0, 2: 1, 3: 0}
DX = {0: 0, 1: 1, 2: 0, 3: -1}
paint = {0: 'Black', 1: 'White'}

facing = 0
count = 0
painted = set()

width = 50
height = 10

grid = [[0 for _ in range(width)] for _ in range(height)]

x = int(width/10)
y = int(height/10)

p_input = [1]

while True:

    print(p_input)

    p_input, finished = computer.software(p_input)

    if finished:
        break

    print("Output is {}".format(p_input))

    facing = (facing + (1 if p_input.pop() == 1 else -1)) % 4

    if grid[y][x] != p_input[0]:
        print("{pos} is {colour1} Painted {pos} {colour2}".format(pos=(x, y), colour1=paint[grid[y][x]], colour2=paint[p_input[0]]))
        grid[y][x] = p_input.pop()
        painted.add((x, y))

    x += DX[facing]
    y += DY[facing]

    p_input.append(grid[y][x])


for y in range(len(grid)):

    for x in range(len(grid[0])):

        if grid[y][x] == 0:
            grid[y][x] = '.'

        grid[y][x] = str(grid[y][x])

for each in grid:
    print("".join(each))


