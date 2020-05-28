
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


def amp_software(intcode, inputs):

    foutput = 0
    fcursor = 0
    input_instruction_counter = 0

    print(intcode)

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

                output_mode = instruction[-3]

                if op == '03':

                    intcode[intcode[fcursor+1]] = inputs[input_instruction_counter]

                    input_instruction_counter += 1

                else:

                    if output_mode == '1':
                        foutput = intcode[fcursor+1]

                    else:
                        foutput = intcode[intcode[fcursor+1]]

                fcursor += 2

        else:
            print("Program halted: Intcode 99, output = {}".format(foutput))
            break

    return foutput


'''

INITIALISING VARIABLES

'''

software = initialize()
p_input = 0
p_output = []
final_outputs = []
cursor = 0
number_of_runs = 0

pc_comb = permutations([0, 1, 2, 3, 4])


'''

BEGIN MAIN FUNCTION

'''

for phases in pc_comb:

    amplifier_out = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

    for index, setting in enumerate(phases):

        amplifier_out[list(amplifier_out.keys())[index]] = amp_software(initialize(), [setting, (0 if index == 0 else amplifier_out[list(amplifier_out.keys())[index-1]])])

    final_outputs.append(amplifier_out['E'])


print(max(final_outputs))



