
with open('phases.txt', 'r') as file:
    A = file.read()

intcode_str = A.split(",")

intcode = []

for string in intcode_str:
    intcode.append(int(string))


def multiple_digit(fcursor):

    instruction = str(intcode[fcursor])

    for _ in range(0, 5 - len(str(intcode[fcursor]))):
        instruction = '0' + instruction

    print("New Instruction = {}".format(instruction))

    op = instruction[-2:]
    num1_mode = instruction[-3]
    num2_mode = instruction[-4]
    move_cursor = 0

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
            move_cursor = 3

    if op == '06':

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
            move_cursor = 3

    if op == '07':

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
            move_cursor = 4
        else:
            intcode[out_address] = 0
            move_cursor = 4

    if op == '08':

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
            move_cursor = 4
        else:
            intcode[out_address] = 0
            move_cursor = 4

    if op == '01' or op == '02':

        move_cursor = 4

        output_mode = instruction[-5]

        if num1_mode == '0':
            num1 = int(intcode[int(intcode[fcursor + 1])])
        else:
            num1 = int(intcode[fcursor+1])

        if num2_mode == '0':
            pos2 = int(intcode[fcursor + 2])
            num2 = int(intcode[pos2])
        else:
            num2 = int(intcode[fcursor + 2])

        if op == '01':
            ans = num1 + num2

        else:
            ans = num1 * num2

        if output_mode == '0':
            intcode[intcode[fcursor+3]] = ans

        else:
            intcode[fcursor+3] = ans

    elif op == '03' or op == '04':

        move_cursor = 2
        output_mode = instruction[-3]

        if op == '03':

            if output_mode == '1':
                intcode[fcursor+1] = p_input

            else:
                intcode[intcode[fcursor+1]] = p_input

        else:

            if output_mode == '1':
                p_output.append(intcode[fcursor+1])

            else:
                p_output.append(intcode[intcode[fcursor+1]])

    return fcursor + move_cursor


p_input = 4
p_output = []
cursor = 0


print("length is {}".format(len(intcode)))

while True:

    if str(intcode[cursor]) != '99':
        print("cursor = {}, instruction ={}".format(cursor, intcode[cursor]))
        cursor = multiple_digit(cursor)

    else:
        print("Program Halted: intcode 99")
        break

print("Output is: {}".format(p_output))

