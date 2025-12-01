def main():
    with open('input.txt') as f:
        data = f.read()

    data = data.split('\n')

    data = [(c[0], int(c[1:])) for c in data]

    dial = 50
    max_dial = 99

    positions_at_zero = 0
    positions_passing_zero = 0

    for direction, clicks in data:
        match direction:
            case 'L':
                direction = -1
            case 'R':
                direction = 1

        for _ in range(clicks):
            dial = (dial + direction) % (max_dial + 1)
            if dial == 0:
                positions_passing_zero += 1

        if dial == 0:
            positions_at_zero += 1

    print(positions_at_zero)
    print(positions_passing_zero)


if __name__ == '__main__':
    main()
