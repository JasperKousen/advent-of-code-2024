from copy import deepcopy

def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    data = [list(row) for row in data]

    parsed_data = deepcopy(data)

    col_size = len(data)
    row_size = len(data[0])

    def count_adjacent_rolls(i, j):
        count = 0
        for x, y in [
            (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
            (i, j - 1), (i, j + 1),
            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
        ]:
            if x < 0 or y < 0:
                continue

            if x >= col_size or y >= row_size:
                continue

            position = data[x][y]

            if position == '@':
                count += 1

        return count

    accessible_rolls = 0
    for i, row in enumerate(data):
        for j, column in enumerate(row):
            if data[i][j] != '@':
                continue

            if count_adjacent_rolls(i, j) < 4:
                accessible_rolls += 1
                parsed_data[i][j] = 'x'

    print('\n'.join(''.join(row) for row in parsed_data))
    print(accessible_rolls)

if __name__ == '__main__':
    main()
