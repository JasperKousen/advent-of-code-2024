import re

import numpy as np


def main():
    with open('input.txt') as f:
        data = f.read()

#     data = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
#
# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176
#
# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450
#
# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279"""

    pattern = r'Button A: X\+(?P<x_a>\d+), Y\+(?P<y_a>\d+)\nButton B: X\+(?P<x_b>\d+), Y\+(?P<y_b>\d+)\nPrize: X=(?P<x_prize>\d+), Y=(?P<y_prize>\d+)'

    # matches = re.finditer(pattern, data)
    # problems = [match.groupdict() for match in matches]

    problems = re.findall(pattern, data)
    problems = map(lambda problem: map(int, problem), problems)

    cost = 0
    for x_a, y_a, x_b, y_b, x_prize, y_prize in problems:
        a = np.array([
            [x_a, x_b],
            [y_a, y_b],
        ])
        b = np.array([x_prize + 10000000000000, y_prize + 10000000000000])

        solution = np.linalg.solve(a, b)
        solution = np.around(solution).astype('int64')

        if np.array_equal(np.matmul(a, solution), b):
            cost += np.dot(solution, [3, 1])

    print(cost)


if __name__ == '__main__':
    main()
