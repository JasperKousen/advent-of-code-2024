from collections import defaultdict
from pprint import pprint

def main():
    with open('input.txt') as f:
        data = f.read()

    banks = [
        [int(battery) for battery in bank]
        for bank in data.split('\n')
    ]

    batteries = defaultdict()
    for i, bank in enumerate(banks):
        bank_length = len(bank)

        max_batteries = 12 * [0]

        def reset_rest_of_battery(from_index):
            for pos in range(from_index + 1, 12):
                max_batteries[pos] = 0

        for j, battery in enumerate(bank):
            for k in range(max(0, 12 - (bank_length - j)), 11):
                if battery > max_batteries[k]:
                    max_batteries[k] = battery
                    reset_rest_of_battery(k)
                    break
            else:
                if battery > max_batteries[-1]:
                    max_batteries[-1] = battery
                    batteries[i] = max_batteries

    print([
        sum(b * (10 ** (11 - x)) for x, b in enumerate(battery))
        for battery in batteries.values()
    ])
    print(sum(
        sum(b * 10 ** (11 - x)  for x, b in enumerate(battery))
        for battery in batteries.values()
    ))

if __name__ == '__main__':
    main()
