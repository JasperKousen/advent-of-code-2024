import itertools
import math
import operator

def concat(a: int, b:int):
    # return a * (10 ** math.ceil(math.log(b, 10))) + b
    return int(str(a) + str(b))

def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

#     data = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20""".splitlines()

    correct_test_values = []

    for line in data:
        line = line.split(' ')
        result = int(line[0].rstrip(':'))
        parts = [int(part) for part in line[1:]]

        combinations = itertools.product([operator.add, operator.mul, concat], repeat=len(parts) - 1)
        for combination in combinations:
            test_result = parts[0]
            for op, part in zip(combination, parts[1:]):
                test_result = op(test_result, part)

            if result == test_result:
                correct_test_values.append(result)
                break

    print(correct_test_values)
    print(sum(correct_test_values))

if __name__ == '__main__':
    main()
