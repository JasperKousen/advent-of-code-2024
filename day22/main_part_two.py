import itertools
from collections import Counter, deque
from functools import cache
from pprint import pprint

from tqdm import tqdm


def mix(a, b):
    return a ^ b


def prune(number):
    return number % 16777216


@cache
def step(number):
    number = mix(number, number * 64)
    number = prune(number)

    number = mix(number, number // 32)
    number = prune(number)

    number = mix(number, number * 2048)
    number = prune(number)

    return number


@cache
def bananas_per_sequence(number, n):
    bananas = {}
    differences = deque(maxlen=4)
    for _ in range(n):
        new_number = step(number)
        differences.append(new_number % 10 - number % 10)
        number = new_number

        if (sequence := tuple(differences)) not in bananas:
            if len(sequence) < 4:
                continue
            bananas[sequence] = number % 10
    return bananas


def main():
    with open('input.txt') as f:
        data = f.read()

    #     data = """1
    # 2
    # 3
    # 2024"""

    numbers = list(map(int, data.splitlines()))

    bananas = Counter()
    for number in numbers:
        bananas.update(bananas_per_sequence(number, 2000))
    pprint(bananas.most_common(10))


if __name__ == '__main__':
    main()
