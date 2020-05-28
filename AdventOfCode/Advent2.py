import numpy as np

noun = 0
verb = 0
count = 0

intcode = np.loadtxt(fname="intcode.txt", delimiter=",")

while intcode[0] != 19690720:

    intcode = np.loadtxt(fname="intcode.txt", delimiter=",")
    intcode[1] = noun
    intcode[2] = verb
    cursor = 0

    print(intcode)

    while cursor <= len(intcode):

        pos1 = int(intcode[cursor + 1])
        pos2 = int(intcode[cursor + 2])
        pos3 = int(intcode[cursor + 3])

        if int(intcode[cursor]) == 1:

            intcode[pos3] = int(intcode[pos1] + intcode[pos2])
            cursor += 4

        elif int(intcode[cursor]) == 2:
            intcode[pos3] = int(intcode[pos1] * intcode[pos2])
            cursor += 4

        elif int(intcode[cursor]) == 99:

            print("noun = {}, verb = {}, output = {}".format(noun, verb, intcode[0]))
            print("Completed")
            break

    if verb != 99:
        verb += 1

    elif verb == 99:
        noun += 1
        verb = 0


print(intcode[0])
