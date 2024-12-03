import re


def part_one():
    with open('input.txt') as f:
        data = f.read()

    multiplications = re.findall(r'mul\((\d+),(\d+)\)', data)

    answer = sum(int(x) * int(y) for x, y in multiplications)
    print(f'Answer Part One: {answer}')


def part_two():
    with open('input.txt') as f:
        data = f.read()

    answer = 0

    do = True
    pos = -1
    while True:
        next_do = data.find('do()', pos + 1)
        next_dont = data.find("don't()", pos + 1)

        if not do:
            if next_do == -1:
                break

            pos = next_do
            do = True
            continue

        next_mul = re.search(r'mul\((\d+),(\d+)\)', data[pos + 1:])
        if next_mul is None:
            break

        while next_dont == -1 or pos + next_mul.start() < next_dont:
            x, y = next_mul.groups()
            answer += int(x) * int(y)
            pos = pos + next_mul.end()

            next_mul = re.search(r'mul\((\d+),(\d+)\)', data[pos + 1:])
            if next_mul is None:
                break

        if next_mul is None:
            break

        do = False
        pos = next_dont

    print(f'Answer Part Two: {answer}')


def main():
    part_one()

    part_two()


if __name__ == '__main__':
    main()
