import functools


@functools.cache
def blink(stone, n):
    if n == 0:
        return 1

    if stone == 0:
        return blink(1, n - 1)
    elif len(stone_string := str(stone)) % 2 == 0:
        split = len(stone_string) // 2
        left_stone, right_stone = stone_string[:split], stone_string[split:]
        return blink(int(left_stone), n - 1) + blink(int(right_stone), n - 1)
    else:
        return blink(2024 * stone, n - 1)


def main():
    data = '7568 155731 0 972 1 6919238 80646 22'
    # data = '125 17'
    data = map(int, data.split(' '))

    n = 75
    result = sum(blink(stone, n) for stone in data)

    print(result)


if __name__ == '__main__':
    import time

    s = time.perf_counter()
    main()
    e = time.perf_counter()
    print(e - s)
