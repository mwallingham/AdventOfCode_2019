
import math
import matplotlib.pyplot as plt

reactions = {}

for line in open('fuel.txt', 'r').readlines():

    line = line.strip()
    line = line.split('=>')

    R = line[0].split(',')
    P = line[1]

    P_quantity, P_name = P.split()
    reactions[(P_name, int(P_quantity))] = {}

    for each in R:
        R_quantity, R_name = each.split()
        reactions[(P_name, int(P_quantity))][R_name] = int(R_quantity)


    print(reactions)


print(reactions)


class reaction:

    def __init__(self, dictionary):
        self.reactions = dictionary
        self.spare = {}

    def get_reactants(self, ask, product, ore=0):

        for R_product in list(self.reactions.keys()):

            if product in R_product:

                if product in list(self.spare.keys()):
                    while self.spare[product] > 0:
                        if ask == 0:
                            break
                        ask -= 1
                        self.spare[product] -= 1

                need = math.ceil(ask / R_product[1])
                spare = need*R_product[1] - ask

                if product not in list(self.spare.keys()):
                    self.spare[product] = spare
                else:
                    self.spare[product] += spare

                for reactant_needed in list(self.reactions[R_product].keys()):

                    if reactant_needed == 'ORE':
                        ore += self.reactions[R_product][reactant_needed] * need

                    ore += self.get_reactants(self.reactions[R_product][reactant_needed] * need, reactant_needed)

        return ore


system = reaction(reactions)

fuel = []
ore = []

for i in range(1000):
    fuel.append(i)
    ore.append(system.get_reactants(i, 'FUEL'))

plt.figure(figsize=(10, 8))
plt.plot(ore, fuel)

print(ore)


