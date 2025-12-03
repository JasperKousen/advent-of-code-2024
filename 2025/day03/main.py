from collections import defaultdict

def main():
    with open('input.txt') as f:
        data = f.read()

    banks = [
        [int(battery) for battery in bank]
        for bank in data.split('\n')
    ]

    max_batteries = defaultdict()
    for i, bank in enumerate(banks):
        bank_length = len(bank)

        max_first_battery = 0
        max_second_battery = 0

        for j, battery in enumerate(bank):
            if (j + 1 != bank_length) and (battery > max_first_battery):
                max_first_battery = battery
                max_second_battery = 0
                continue

            if battery > max_second_battery:
                max_second_battery = battery
                max_batteries[i] = (max_first_battery, max_second_battery)
                continue

    print(max_batteries)
    print(sum(
        batteries[0] * 10 + batteries[1]
        for batteries in max_batteries.values()
    ))

if __name__ == '__main__':
    main()
