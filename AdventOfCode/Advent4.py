

def ascending(number):

    highest = int(number[0])

    for pos in number:

        if int(pos) < highest:
            return False

        else:
            highest = int(pos)

    return True


def double(number):

    rep_counter = -1
    streak = []
    char = number[0]

    for pos in number:

        if pos == char:
            rep_counter += 1

        elif pos != char:
            streak.append(rep_counter)
            rep_counter = 0
            char = pos

    streak.append(rep_counter)

    if 1 in streak:
        print(streak)
        return True
    else:
        return False


r_input = "273025-767253"

r_low, r_up = r_input.split("-")

possibles = []

for num in range(int(r_low), int(r_up) + 1):

    if ascending(str(num)) and double(str(num)):

        possibles.append(num)

print(len(possibles))



