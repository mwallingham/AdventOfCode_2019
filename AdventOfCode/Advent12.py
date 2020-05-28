
import numpy as np
from operator import sub, add


def get_data(filename):

    with open(filename, 'r') as file:

        a = file.read()
        a = [line for line in a.split("\n")]
        a = [line[1:-1] for line in a]
        a = [line.split(",") for line in a]

    for coords in range(len(a)):
        for coord in range(len(a[0])):
            a[coords][coord] = int(a[coords][coord].split("=")[-1])

    return a


class system:

    def __init__(self):
        self.time = 0
        self.moon_list = {}
        self.gravity = 1

    def add_moon(self, pos, vel=(0, 0, 0)):
        self.moon_list['Moon ' + str(len(self.moon_list) + 1)] = self.moon(pos, vel)

    def display(self):

        print("Timestep = {}".format(self.time))

        for k, v in self.moon_list.items():
            print("{} is in position {}, velocity {}".format(k, v.position, v.velocity))

    def get_gravity(self, moon1, moon2):

        acceleration = [0, 0, 0]

        for axis in range(len(moon1)):

            if moon2[axis] > moon1[axis]:
                acceleration[axis] = 1
            elif moon1[axis] > moon2[axis]:
                acceleration[axis] = -1
            else:
                acceleration[axis] = 0

        return acceleration

    def set_velocities(self):

        moons = list(self.moon_list.values())

        for i in range(len(moons)):
            t_gravity = [0, 0, 0]
            for j in range(len(moons) - 1):
                t_gravity = map(add, t_gravity,
                                self.get_gravity(moons[i].position, moons[(i+j+1) % len(moons)].position))

            moons[i].velocity = list(map(add, moons[i].velocity, t_gravity))

    def set_positions(self):

        moons = list(self.moon_list.values())

        for i in range(len(moons)):
            moons[i].position = list(map(add, moons[i].velocity, moons[i].position))

    def step_time(self, time_step=1):

        self.display()

        for _ in range(time_step):

            self.set_velocities()
            self.set_positions()
            self.time += 1
            print(self.time)
        self.display()

    def energy(self):

        moons = list(self.moon_list.values())
        total_e = 0

        for i in range(len(moons)):

            t_k_energy = [0, 0, 0]
            t_p_energy = [0, 0, 0]

            for j in range(3):
                t_k_energy[j] += abs(moons[i].velocity[j])
                t_p_energy[j] += abs(moons[i].position[j])

            print(sum(t_p_energy), sum(t_k_energy))
            total_e += sum(t_k_energy) * sum(t_p_energy)

        return total_e

    class moon:
        def __init__(self, pos, vel):
            self.position = pos
            self.velocity = vel


positions = get_data('moons.txt')

moon_system = system()

for position in positions:
    moon_system.add_moon(position)


moon_system.step_time(1000000)

print(moon_system.energy())

