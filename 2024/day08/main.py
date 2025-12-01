import itertools


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

#     data = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............""".splitlines()

    data = [list(line) for line in data]

    max_y = len(data)
    max_x = len(data[0])

    unique_frequencies = set()

    for line in data:
        unique_frequencies.update(set(line) - {'.'})

    unique_antinodes = set()

    for frequency in unique_frequencies:
        positions = []
        for i, line in enumerate(data):
            try:
                j = line.index(frequency)
                positions.append((i, j))
            except ValueError:
                continue

        for antenna_1, antenna_2 in itertools.combinations(positions, 2):
            d = (antenna_1[0] - antenna_2[0], antenna_1[1] - antenna_2[1])

            antinode_1 = (antenna_1[0] + d[0], antenna_1[1] + d[1])
            antinode_2 = (antenna_2[0] - d[0], antenna_2[1] - d[1])

            if 0 <= antinode_1[0] <= max_y - 1 and 0 <= antinode_1[1] <= max_x - 1:
                unique_antinodes.add(antinode_1)

            if 0 <= antinode_2[0] <= max_y - 1 and 0 <= antinode_2[1] <= max_x - 1:
                unique_antinodes.add(antinode_2)

    print(unique_antinodes)
    print(len(unique_antinodes))

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != '.':
                continue

            if (i, j) in unique_antinodes:
                data[i][j] = '#'
    data = '\n'.join(''.join(line) for line in data)
    print(data)

if __name__ == '__main__':
    main()