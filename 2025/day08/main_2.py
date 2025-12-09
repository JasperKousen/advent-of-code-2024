from collections import defaultdict
from functools import cache
from hmac import digest_size
from itertools import permutations
from math import sqrt, prod
from pprint import pprint

@cache
def distance(box1, box2):
    return sqrt(
        (box1[0] - box2[0]) ** 2
        + (box1[1] - box2[1]) ** 2
        + (box1[2] - box2[2]) ** 2
    )

def main():
    with open('input.txt') as f:
        data = f.readlines()

    boxes = [
        tuple(int(c) for c in b.strip().split(','))
        for b in data
    ]

    distances = {
        (box1, box2): distance(box1, box2)
        for box1 in boxes
        for box2 in boxes
        if box1 != box2
    }

    circuits = []

    while distances:
        closest = min(distances.items(), key=lambda x: x[1])[0]
        distances.pop(closest)
        distances.pop(tuple(reversed(closest)))

        extended_circuits = []
        for circuit in circuits:
            if closest[0] in circuit or closest[1] in circuit:
                circuit.update(set(closest))

                extended_circuits.append(circuit)

            if extended_circuits == 2:
                break

        if not extended_circuits:
            circuits.append(set(closest))

        if len(extended_circuits) > 1:
            for circuit in extended_circuits:
                circuits.pop(circuits.index(circuit))

            circuits.append(set().union(*extended_circuits))

        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            break

    pprint(circuits)
    print(closest)
    print(closest[0][0] * closest[1][0])

if __name__ == '__main__':
    main()
