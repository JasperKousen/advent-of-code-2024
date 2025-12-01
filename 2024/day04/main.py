import itertools


def catch_index_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return False

    return inner


@catch_index_error
def check(
        data: list,
        i: int,
        j: int,
        horizontal: int,
        vertical: int,
        max_i: int,
        max_j: int,
):
    if data[i][j] != 'X':
        return False

    y, x = i + 1 * vertical, j + 1 * horizontal
    if y < 0 or y >= max_i or x < 0 or x >= max_j:
        return False
    if data[y][x] != 'M':
        return False

    y, x = i + 2 * vertical, j + 2 * horizontal
    if y < 0 or y >= max_i or x < 0 or x >= max_j:
        return False
    if data[y][x] != 'A':
        return False

    y, x = i + 3 * vertical, j + 3 * horizontal
    if y < 0 or y >= max_i or x < 0 or x >= max_j:
        return False
    if data[y][x] != 'S':
        return False

    return True


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

#     data = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX""".splitlines()

    rows = len(data)
    cols = len(data[0])

    count = 0

    for i in range(rows):
        for j in range(cols):
            x = data[i][j]

            if x != 'X':
                continue

            for horizontal, vertical in itertools.product([-1, 0, 1], [-1, 0, 1]):
                if check(data, i, j, horizontal, vertical, max_i=rows, max_j=cols):
                    print((i, j, horizontal, vertical))
                    count += 1
    print(count)


if __name__ == '__main__':
    main()
