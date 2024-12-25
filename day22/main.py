from functools import cache
from pprint import pprint

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
def steps(number, n):
    for _ in range(n):
        number = step(number)
    return number

    # if n == 0:
    #     return number
    #
    # return steps(step(number), n-1)

def main():
    with open('input.txt') as f:
        data = f.read()

#     data = """1
# 10
# 100
# 2024"""

    numbers = list(map(int, data.splitlines()))

    pprint([steps(123, n) for n in range(11)])

    steps_2000 = {number: steps(number, 2000) for number in numbers}
    pprint(steps_2000)
    print(sum(steps_2000.values()))


if __name__ == '__main__':
    main()