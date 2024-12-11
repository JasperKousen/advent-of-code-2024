blinks = dict()


def blink(stone, n):
    if n == 0:
        return 1

    try:
        return blinks[(stone, n)]
    except KeyError:
        stones = []

        if stone == 0:
            stones.append(1)
        elif len(stone_string := str(stone)) % 2 == 0:
            split = len(stone_string) // 2
            left_stone, right_stone = stone_string[:split], stone_string[split:]
            stones.append(int(left_stone))
            stones.append(int(right_stone))
        else:
            stones.append(2024 * stone)

        blinks[(stone, n)] = sum(blink(s, n - 1) for s in stones)
        return blinks[(stone, n)]


def main():
    data = '7568 155731 0 972 1 6919238 80646 22'
    # data = '125 17'
    data = data.split(' ')
    data = [int(stone) for stone in data]

    n = 75
    result = sum(blink(stone, n) for stone in data)

    print(result)


if __name__ == '__main__':
    main()
