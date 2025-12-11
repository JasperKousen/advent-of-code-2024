import numpy as np
from scipy import optimize

def main():
    with open('input_test.txt') as f:
        data = f.read()
    data = [row.split(' ') for row in data.splitlines()]

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

        print(machine)
        print(buttons)
        # print(joltage)

        print(buttons.T.dot(np.ones(buttons.shape[0])))

        # res = optimize.milp(
        #     c=np.ones(buttons.shape[0]),
        #     bounds=optimize.Bounds(lb=0),
        #     constraints=optimize.LinearConstraint(
        #         buttons,
        #         lb=machine,
        #         ub=machine,
        #     )
        # )

        # print(res)


if __name__ == '__main__':
    main()
