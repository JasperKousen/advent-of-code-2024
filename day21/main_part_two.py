import itertools
import operator
from functools import cache


@cache
def directional_keypad_coordinates(button):
    match button:
        case '<':
            return 0, 0
        case 'v':
            return 0, 1
        case '>':
            return 0, 2
        case '^':
            return 1, 1
        case 'A':
            return 1, 2


@cache
def numeric_keypad_coordinates(button):
    match button:
        case '0':
            return 0, 1
        case 'A':
            return 0, 2
        case _:
            value = int(button)
            return (value - 1) // 3 + 1, (value - 1) % 3,


@cache
def is_valid_step(step, y, x, directional=True):
    for s in step:
        match s:
            case '^':
                y, x = y + 1, x
            case '>':
                y, x = y, x + 1
            case 'v':
                y, x = y - 1, x
            case '<':
                y, x = y, x - 1

        if directional:
            if (y, x) == (1, 0):
                return False
        else:
            if (y, x) == (0, 0):
                return False
    else:
        return True


@cache
def get_steps(from_coordinates, to_coordinates, directional=True):
    step = ''
    if to_coordinates[1] < from_coordinates[1]:
        s = '<'
    else:
        s = '>'
    step += s * abs(to_coordinates[1] - from_coordinates[1])

    if to_coordinates[0] < from_coordinates[0]:
        s = 'v'
    else:
        s = '^'
    step += s * abs(to_coordinates[0] - from_coordinates[0])

    steps = set(''.join(i) for i in itertools.permutations(step))
    steps = tuple(step + 'A' for step in steps if is_valid_step(step, *from_coordinates, directional))
    return steps


@cache
def quickest_steps(code, iterations, total_iterations):
    directional = iterations < total_iterations
    keypad_coordinates = directional_keypad_coordinates if directional else numeric_keypad_coordinates
    code = 'A' + code

    instruction_size = 0
    if not iterations:
        for from_button, to_button in zip(code, code[1:]):
            from_coordinates = keypad_coordinates(from_button)
            to_coordinates = keypad_coordinates(to_button)
            steps = get_steps(from_coordinates, to_coordinates, directional)

            instruction_size += len(steps[0])
        return instruction_size

    for from_button, to_button in zip(code, code[1:]):
        from_coordinates = keypad_coordinates(from_button)
        to_coordinates = keypad_coordinates(to_button)
        steps = get_steps(from_coordinates, to_coordinates, directional)

        instruction_size += min(quickest_steps(step, iterations - 1, total_iterations) for step in steps)
    return instruction_size


def main():
    with open('input.txt') as f:
        data = f.read()

    #     data = """029A
    # 980A
    # 179A
    # 456A
    # 379A"""

    codes = data.splitlines()
    print(codes)

    instruction_sizes = [quickest_steps(code, 25, total_iterations=25) for code in codes]
    print(instruction_sizes)

    complexities = [
        (size, int(code[:3]))
        for size, code in zip(instruction_sizes, codes)
    ]
    print(complexities)
    print(sum(operator.mul(*complexity) for complexity in complexities))


if __name__ == '__main__':
    main()
