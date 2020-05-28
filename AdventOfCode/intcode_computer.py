
class intcode_computer:

    def __init__(self, program, output_length):
        self.fcursor = 0
        self.r_base = 0
        self.output_length = output_length
        self.program = program
        self.copy_of_program = [_ for _ in program]

    def get_numbers(self, num1_m, num2_m, output_mode=None):

        if num1_m == '0':
            num1 = self.program[self.program[self.fcursor + 1]]
        elif num1_m == '1':
            num1 = self.program[self.fcursor + 1]
        else:
            num1 = self.program[self.r_base + self.program[self.fcursor + 1]]

        if num2_m == '0':
            num2 = self.program[self.program[self.fcursor + 2]]
        elif num2_m == '1':
            num2 = self.program[self.fcursor + 2]
        else:
            num2 = self.program[self.r_base + self.program[self.fcursor + 2]]

        if output_mode is not None:

            if output_mode != '2':
                ad3 = self.program[self.fcursor + 3]
            else:
                ad3 = self.r_base + self.program[self.fcursor + 3]

            return num1, num2, ad3

        else:
            return num1, num2

    def software(self, inputs=None):

        foutput = []

        done = False

        while True:

            if str(self.program[self.fcursor]) != '99':

                instruction = str(self.program[self.fcursor])

                for _ in range(0, 5 - len(str(self.program[self.fcursor]))):
                    instruction = '0' + instruction

                op = instruction[-2:]
                num1 = None
                num2 = None
                num1_mode = instruction[-3]
                num2_mode = instruction[-4]
                output_mode = instruction[-5]
                ad3 = None

                if op in ['05', '06', '09']:
                    num1, num2 = self.get_numbers(num1_mode, num2_mode)

                elif op in ['03', '04']:
                    if num1_mode == '0':
                        ad3 = self.program[self.fcursor + 1]
                    elif num1_mode == '1':
                        ad3 = self.fcursor + 1
                    else:
                        ad3 = self.r_base + self.program[self.fcursor + 1]

                else:
                    num1, num2, ad3 = self.get_numbers(num1_mode, num2_mode, output_mode)

                if op == '05':

                    if num1 != 0:
                        self.fcursor = int(num2)
                    else:
                        self.fcursor += 3

                elif op == '09':
                    self.r_base += num1
                    self.fcursor += 2

                elif op == '06':
                    if num1 == 0:
                        self.fcursor = int(num2)
                    else:
                        self.fcursor += 3

                elif op == '07':

                    if num1 < num2:
                        self.program[ad3] = 1
                    else:
                        self.program[ad3] = 0

                    self.fcursor += 4

                elif op == '08':
                    if num1 == num2:
                        self.program[ad3] = 1
                    else:
                        self.program[ad3] = 0

                    self.fcursor += 4

                elif op == '01':
                    self.program[ad3] = num1 + num2
                    self.fcursor += 4

                elif op == '02':

                    self.program[ad3] = num2 * num1
                    self.fcursor += 4

                elif op == '03':
                    self.program[ad3] = inputs.pop()
                    self.fcursor += 2

                elif op == '04':
                    foutput.append(self.program[ad3])
                    self.fcursor += 2
                    if len(foutput) == self.output_length:
                        return foutput, done

                else:

                    print("ERROR, OPCODE {} RECEIVED".format(op))
                    break

            else:
                done = True
                break

        return foutput, done

    def reboot(self, new_program=None):

        if new_program is not None:
            self.program = new_program

        else:
            self.program = [_ for _ in self.copy_of_program]
