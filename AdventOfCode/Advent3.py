
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def get_points(a):

    x = 0
    y = 0
    length = 0

    ans = {}

    for cmd in a:
        d = cmd[0]
        n = int(cmd[1:])
        for _ in range(n):
            x += DX[d]
            y += DY[d]
            length += 1

            if (x, y) not in ans:

                ans[(x, y)] = length

    return ans


with open('directions.txt', 'r') as file:
    A, B = file.read().split("\n")

A, B = [x.split(",") for x in [A, B]]

PA = get_points(A)
PB = get_points(B)

both = set(PA.keys()) & set(PB.keys())

best = min([PA[p] + PB[p] for p in both])

print(best)

