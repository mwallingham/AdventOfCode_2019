
def get_parents(orbits_remaining):

    unique_orbits = {}

    for pair in orbits_remaining:

        if pair[0] not in unique_orbits.keys():
            unique_orbits[pair[0]] = []

        unique_orbits[pair[0]].append(pair[1])

    return unique_orbits


def count_paths(orbit_parents, x):

    answer = 0

    for y in orbit_parents.get(x, []):

        answer += count_paths(orbit_parents, y)
        answer += 1

    return answer


with open('orbits.txt', 'r') as file:
    A = file.read()

raw_orbits = A.split("\n")
orbits = []

for orbit in raw_orbits:
    orbits.append(orbit.split(")"))


parents = get_parents(orbits)

ans = 0

for x in parents:
    ans += count_paths(parents, x)

print(ans)


