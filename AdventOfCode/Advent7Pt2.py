
from itertools import permutations
import time


def initialize():

    with open('phases.txt', 'r') as file:
        a = file.read()

    intcode_str = a.split(",")

    intcode_init = []

    for string in intcode_str:
        intcode_init.append(int(string))

    return intcode_init


def amp_software(intcode, inputs, pass_cursor):

    fcursor = pass_cursor

    print("Inputs are: {}".format(inputs))

    while True:

        if str(intcode[fcursor]) != '99':

            instruction = str(intcode[fcursor])

            for _ in range(0, 5 - len(str(intcode[fcursor]))):
                instruction = '0' + instruction

            op = instruction[-2:]
            num1_mode = instruction[-3]
            num2_mode = instruction[-4]

            if op == '05':

                if num1_mode == '0':
                    num1 = intcode[intcode[fcursor+1]]
                else:
                    num1 = intcode[fcursor+1]

                if num2_mode == '0':
                    num2 = intcode[intcode[fcursor + 2]]
                else:
                    num2 = intcode[fcursor+2]

                if num1 != 0:
                    fcursor = int(num2)
                else:
                    fcursor += 3

            elif op == '06':

                if num1_mode == '0':
                    num1 = intcode[int(intcode[fcursor + 1])]
                else:
                    num1 = intcode[fcursor + 1]

                if num2_mode == '0':
                    num2 = intcode[int(intcode[fcursor + 2])]
                else:
                    num2 = intcode[fcursor + 2]

                if num1 == 0:

                    fcursor = int(num2)

                else:
                    fcursor += 3

            elif op == '07':

                output_mode = instruction[-5]

                if num1_mode == '0':
                    num1 = intcode[int(intcode[fcursor + 1])]
                else:
                    num1 = intcode[fcursor + 1]

                if num2_mode == '0':
                    num2 = intcode[int(intcode[fcursor + 2])]
                else:
                    num2 = intcode[fcursor + 2]

                if output_mode == '0':
                    out_address = intcode[fcursor+3]

                else:
                    out_address = fcursor + 3

                if num1 < num2:
                    intcode[out_address] = 1
                    fcursor += 4
                else:
                    intcode[out_address] = 0
                    fcursor += 4

            elif op == '08':

                output_mode = instruction[0]

                if num1_mode == '0':
                    num1 = intcode[int(intcode[fcursor + 1])]
                else:
                    num1 = intcode[fcursor + 1]

                if num2_mode == '0':
                    num2 = intcode[intcode[fcursor + 2]]
                else:
                    num2 = intcode[fcursor + 2]

                if output_mode == '0':
                    out_address = intcode[fcursor + 3]

                else:
                    out_address = fcursor + 3

                if num1 == num2:
                    intcode[out_address] = 1
                    fcursor += 4
                else:
                    intcode[out_address] = 0
                    fcursor += 4

            elif op == '01' or op == '02':

                output_mode = instruction[-5]

                if num1_mode == '0':
                    num1 = intcode[intcode[fcursor + 1]]
                else:
                    num1 = intcode[fcursor+1]

                if num2_mode == '0':
                    pos2 = intcode[fcursor + 2]
                    num2 = intcode[pos2]
                else:
                    num2 = intcode[fcursor + 2]

                if op == '01':
                    ans = num1 + num2

                else:
                    ans = num1 * num2

                if output_mode == '0':
                    intcode[intcode[fcursor+3]] = ans

                else:
                    intcode[fcursor+3] = ans

                fcursor += 4

            else:

                if op == '03':
                    intcode[intcode[fcursor+1]] = inputs.pop(0)
                    fcursor += 2

                else:

                    foutput = intcode[intcode[fcursor+1]]
                    fcursor += 2
                    return foutput, fcursor

        else:
            return None, fcursor


'''

INITIALISING VARIABLES

'''

software = initialize()
p_input = 0
p_output = []
final_outputs = []
cursor = 0
number_of_runs = 0
pc_comb = permutations([5, 6, 7, 8, 9])

'''

BEGIN MAIN FUNCTION

'''

ans = 0

for phases in pc_comb:

    val_pass = 0
    CURSOR = [0 for _ in range(len(phases))]
    VAL = [0 for _ in range(len(phases))]
    Q = [[phases[i]] for i in range(len(phases))]
    Q[0].append(0)
    done = False

    while not done:

        for i in range(len(phases)):

            val, new_cursor = amp_software(initialize(), Q[i], CURSOR[i])

            if val is None:

                print(phases, VAL[-1])

                if VAL[-1] > ans:

                    ans = VAL[-1]

                done = True
                break

            CURSOR[i] = new_cursor

            if val is not None:
                VAL[i] = val

            Q[(i+1) % len(Q)].append(val)

print(ans)


