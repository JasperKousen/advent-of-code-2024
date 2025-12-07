from functools import reduce


def main():
    with open('input.txt') as f:
        data = f.readlines()

    data = [row.strip('\n') for row in data]

    prev_col = 0
    prev_operation = data[-1][0]
    total = 0
    for col, operation in enumerate(data[-1][1:]):
        if operation == ' ':
            continue

        numbers = [
            ''.join(r[c] for r in data[:-1]).strip()
            for c in range(prev_col, col)
        ]

        numbers = [int(n) for n in numbers if n]
        print(numbers)

        match prev_operation:
            case '+':
                total += sum(numbers)
            case '*':
                total += reduce(lambda i,j: i * j, numbers)

        prev_col = col
        prev_operation = operation
    else:
        numbers = []
        for c in range(prev_col, len(data[-2])):
            number_parts = []
            for r in data[:-1]:
                try:
                    number_parts.append(r[c])
                except IndexError:
                    continue

            numbers.append(''.join(number_parts).strip())

        numbers = [int(n) for n in numbers if n]
        print(numbers)

        match prev_operation:
            case '+':
                total += sum(numbers)
            case '*':
                total += reduce(lambda i,j: i * j, numbers)


    print(total)

    # data = [[col.strip() for col in row if col.strip()] for row in data]
    #
    # total = 0
    # for problem in list(zip(*data)):
    #     numbers = [int(n) for n in problem[:-1]]
    #     match problem[-1]:
    #         case '+':
    #             total += sum(numbers)
    #         case '*':
    #             total += reduce(lambda i,j: i * j, numbers)
    #
    # print(total)

if __name__ == '__main__':
    main()
