
import math
import numpy as np
import time

p_dic = {}


a = open("asteroids.txt", 'r').read()

field = [z for z in a.split("\n")]

field_size = (int(len(field[0])), int(len(field)))


def unit_vector(x, y):

    mag = math.sqrt(x ** 2 + y ** 2)
    phi = -np.arctan2(-x, -y)*180/np.pi
    if phi < 0:
        phi += 360

    if phi == -0.0:
        phi = 0.0

    return round(x / mag, 10), round(y / mag, 10), round(phi, 10)


def count_unit_vectors(position, request=False):

    visible = []
    pos_angle = {}

    for y in range(field_size[1]):

        for x in range(field_size[0]):

            if (x, y) != position:
                if field[y][x] == '#':
                    x_unit, y_unit, phi = unit_vector(x - position[0], y - position[1])

                    if (x_unit, y_unit) not in visible:
                        visible.append((x_unit, y_unit))
                        pos_angle[(x, y)] = phi

    p_dic[position] = len(visible)

    if request:
        return pos_angle


for layer in range(field_size[1]):

    for col in (range(field_size[0])):

        if field[layer][col] == '#':

            count_unit_vectors((col, layer))


start = list(p_dic.keys())[list(p_dic.values()).index(max(p_dic.values()))]

count = 0
dummy_field = []
vaporised = (0, 0)

for each in field:
    dummy_field.append([point for point in each])

field = dummy_field


while True:

    positions = count_unit_vectors(start, True)

    for asteroid in sorted(list(positions.values())):

        x_vap, y_vap = list(positions.keys())[list(positions.values()).index(asteroid)]

        field[y_vap][x_vap] = '.'

        count += 1
        vaporised = (x_vap, y_vap)

        if count == 200:
            break

    if count == 200:
        break

print(vaporised)
