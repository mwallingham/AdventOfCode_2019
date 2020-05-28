
import time
from arcade import arcade_computer



def initialize():

    with open('arcade.txt', 'r') as file:
        a = file.read()

    intcode_str = a.split(",")

    intcode_init = []

    for string in intcode_str:
        intcode_init.append(int(string))

    extra_mem = [0 for _ in range(100000)]

    return intcode_init + extra_mem

arcade = arcade_computer(initialize(), 3)

arcade.program[0] = 2

finished = False

grid = [['.' for _ in range(40)] for _ in range(20)]


while not finished:

    finished = arcade.software()

    if finished:

        break



block = 0

