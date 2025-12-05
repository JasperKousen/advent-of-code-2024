from collections import defaultdict
from copy import deepcopy

def adjacent_cells(i, j):
    return [
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
        (i, j - 1), (i, j + 1),
        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
    ]

def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    data = [list(row) for row in data]

    parsed_data = deepcopy(data)

    col_size = len(data)
    row_size = len(data[0])

    def count_adjacent_rolls(i, j):
        count = 0
        for x, y in adjacent_cells(i, j):
            if x < 0 or y < 0:
                continue

            if x >= col_size or y >= row_size:
                continue

            position = data[x][y]

            if position == '@':
                count += 1

        return count

    adjacent_rolls = {}
    for i, row in enumerate(data):
        for j, column in enumerate(row):
            if data[i][j] != '@':
                continue

            adjacent_rolls[(i, j)] = count_adjacent_rolls(i, j)

    number_of_rolls_removed = 0
    to_remove = [None]
    while to_remove:

        to_remove = []
        for (i, j), rolls in adjacent_rolls.items():
            if rolls >= 4:
                continue

            to_remove.append((i, j))

            for x, y in adjacent_cells(i, j):
                if (x, y) in adjacent_rolls:
                    adjacent_rolls[(x, y)] -= 1

        print(len(to_remove))
        for x, y in to_remove:
            adjacent_rolls.pop((x, y))
            parsed_data[i][j] = 'x'
            number_of_rolls_removed += 1


    print('\n'.join(''.join(row) for row in parsed_data))
    print(number_of_rolls_removed)

if __name__ == '__main__':
    main()
