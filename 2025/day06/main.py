from functools import reduce


def main():
    with open('input.txt') as f:
        data = f.readlines()

    data = [row.split(' ') for row in data]
    data = [[col.strip() for col in row if col.strip()] for row in data]

    total = 0
    for problem in list(zip(*data)):
        numbers = [int(n) for n in problem[:-1]]
        match problem[-1]:
            case '+':
                total += sum(numbers)
            case '*':
                total += reduce(lambda i,j: i * j, numbers)

    print(total)

if __name__ == '__main__':
    main()
