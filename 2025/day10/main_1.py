import time

import numpy as np
import cvxpy as cp

def main():
    with open('input.txt') as f:
        data = f.read()
    data = [row.split(' ') for row in data.splitlines()]

    result = 0
    for row in data:
        machine = row[0]
        machine = [0 if s == '.' else 1 for s in machine[1:-1]]

        buttons = row[1:-1]
        buttons = [
            [
                1 if str(i) in button[1:-1].split(',') else 0
             for i in range(len(machine))
            ]
            for button in buttons
        ]
        # joltage = row[-1]

        machine = np.array(machine)  # [l x 1]
        buttons = np.array(buttons)  # [b x l]

        # print(machine)
        # print(buttons)
        # print(joltage)

        presses = cp.Variable(len(buttons), integer=True)
        k = cp.Variable(len(machine), integer=True)

        objective = cp.Minimize(cp.sum(presses))
        constraints = [
            0 <= presses,
            presses <= 1,
            buttons.T @ presses == machine + 2 * k
        ]
        prob = cp.Problem(objective, constraints)

        result += prob.solve()

    print(result)


if __name__ == '__main__':
    s = time.perf_counter()
    main()
    print(time.perf_counter() - s)
