
import time


def initialize():

    with open('paint.txt', 'r') as file:
        a = file.read()

    intcode_str = a.split(",")

    intcode_init = []

    for string in intcode_str:
        intcode_init.append(int(string))

    extra_mem = [0 for _ in range(100000)]

    return intcode_init + extra_mem


program = initialize()


def get_numbers(relative_base, cursor, num1_m, num2_m, output_mode=None):

    if num1_m == '0':
        num1 = program[program[cursor + 1]]
    elif num1_m == '1':
        num1 = program[cursor + 1]
    else:
        num1 = program[relative_base + program[cursor + 1]]

    if num2_m == '0':
        num2 = program[program[cursor + 2]]
    elif num2_m == '1':
        num2 = program[cursor + 2]
    else:
        num2 = program[relative_base + program[cursor + 2]]

    if output_mode is not None:

        if output_mode != '2':
            ad3 = program[cursor + 3]
        else:
            ad3 = relative_base + program[cursor + 3]

        return num1, num2, ad3

    else:
        return num1, num2


def amp_software(inputs):

    foutput = []
    fcursor = 0
    r_base = 0

    while True:

        if str(program[fcursor]) != '99':

            instruction = str(program[fcursor])

            for _ in range(0, 5 - len(str(program[fcursor]))):
                instruction = '0' + instruction

            op = instruction[-2:]
            num1_mode = instruction[-3]
            num2_mode = instruction[-4]
            output_mode = instruction[-5]
            ad3 = None

            if num1_mode == '2':

                print("relative base is {}".format(r_base))

            print("OP = {}, instruction is {}".format(op, instruction))

            if op in ['05', '06', '09']:
                num1, num2 = get_numbers(r_base, fcursor, num1_mode, num2_mode)

            elif op in ['03', '04']:
                if num1_mode != '2':
                    ad3 = program[fcursor + 1]
                else:
                    ad3 = r_base + program[fcursor + 1]

            else:
                num1, num2, ad3 = get_numbers(r_base, fcursor, num1_mode, num2_mode, output_mode)

            # Do not require memory

            if op == '05':

                if num1 != 0:
                    fcursor = int(num2)
                else:
                    fcursor += 3

            elif op == '09':

                print("adjust by: {}".format(num1))
                r_base += num1
                fcursor += 2

            elif op == '06':
                if num1 == 0:
                    fcursor = int(num2)
                else:
                    fcursor += 3

            # Require Memory

            elif op == '07':

                if num1 < num2:
                    program[ad3] = 1
                else:
                    program[ad3] = 0

                fcursor += 4

            elif op == '08':
                if num1 == num2:
                    program[ad3] = 1
                else:
                    program[ad3] = 0

                fcursor += 4

            elif op == '01' or op == '02':

                if op == '01':
                    program[ad3] = num1 + num2

                else:
                    program[ad3] = num2 * num1

                fcursor += 4

            elif op == '03' or op == '04':
                if op == '03':
                    program[ad3] = inputs.pop()

                else:
                    foutput.append(program[ad3])
                    print("output is {}".format(foutput))
                fcursor += 2

            else:

                print("ERROR, OPCODE {} RECEIVED".format(op))
                break

        else:

            break

    return foutput


print(amp_software([2]))
