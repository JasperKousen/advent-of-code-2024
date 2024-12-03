import re
from collections import Counter


def main():
    left, right = [], []

    with open('input.txt') as f:
        for line in f.read().splitlines():
            line = re.findall(r'\d+', line)

            left.append(int(line[0]))
            right.append(int(line[1]))

    left, right = sorted(left), sorted(right)

    answer_part_one = sum(abs(l - r) for l, r in zip(left, right))

    print(f'Answer Part One: {answer_part_one}')

    right_counts = Counter(right)

    answer_part_two = sum(l * right_counts[l] for l in left)

    print(f'Answer Part Two: {answer_part_two}')

if __name__ == '__main__':
    main()
