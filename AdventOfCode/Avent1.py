
import numpy as np

masses = list(np.loadtxt(fname="masses.txt"))
total = 0
error = 100

for mass in masses:

    extra = 1
    fuel = int(mass / 3) - 2
    total += fuel

    while extra > 0:

        extra = int(fuel/3) - 2

        if extra > 0:
            total += extra

        fuel = extra

print(total)




