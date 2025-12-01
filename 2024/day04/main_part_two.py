import itertools


def check(
        data: list,
        i: int,
        j: int,
):
    p, q, r, s = data[i - 1][j - 1], data[i - 1][j + 1], data[i + 1][j + 1], data[i + 1][j - 1]

    if p + q + r + s in ['MMSS', 'SMMS', 'SSMM', 'MSSM']:
        return True

    return False


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

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            x = data[i][j]

            if x != 'A':
                continue

            if check(data, i, j):
                print((i, j))
                count += 1
    print(count)


if __name__ == '__main__':
    main()
