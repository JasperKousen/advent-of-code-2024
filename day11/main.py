def main():
    data = '7568 155731 0 972 1 6919238 80646 22'
    # data = '125 17'
    data = data.split(' ')
    data = [int(stone) for stone in data]

    prev_output = data
    output = []
    for i in range(25):
        print(i)
        output = []
        for stone in prev_output:
            if stone == 0:
                output.append(1)
            elif len(stone_string := str(stone)) % 2 == 0:
                split = len(stone_string) // 2
                left_stone, right_stone = stone_string[:split], stone_string[split:]
                output.append(int(left_stone))
                output.append(int(right_stone))
            else:
                output.append(2024 * stone)

        prev_output = output.copy()

    print(output)
    print(len(output))


if __name__ == '__main__':
    main()
