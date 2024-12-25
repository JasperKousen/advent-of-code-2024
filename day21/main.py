import itertools
import operator
from pprint import pprint
from functools import cache


# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

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
    instruction = ''
    if to_coordinates[1] < from_coordinates[1]:
        step = '<'
    else:
        step = '>'
    instruction += step * abs(to_coordinates[1] - from_coordinates[1])

    if to_coordinates[0] < from_coordinates[0]:
        step = 'v'
    else:
        step = '^'
    instruction += step * abs(to_coordinates[0] - from_coordinates[0])

    steps = set(''.join(i) for i in itertools.permutations(instruction))
    steps = tuple(step + 'A' for step in steps if is_valid_step(step, *from_coordinates, directional))
    return steps


@cache
def quickest_steps(code, iterations):
    directional = iterations < 2
    keypad_coordinates = directional_keypad_coordinates if directional else numeric_keypad_coordinates
    code = 'A' + code

    instructions = [''] * (iterations + 1)
    if not iterations:
        for from_button, to_button in zip(code, code[1:]):
            from_coordinates = keypad_coordinates(from_button)
            to_coordinates = keypad_coordinates(to_button)
            steps = get_steps(from_coordinates, to_coordinates, directional)

            if steps:
                instructions[0] += steps[0]
        return instructions

    for from_button, to_button in zip(code, code[1:]):
        from_coordinates = keypad_coordinates(from_button)
        to_coordinates = keypad_coordinates(to_button)
        steps = get_steps(from_coordinates, to_coordinates, directional)

        if steps:
            steps = {step: quickest_steps(step, iterations=iterations - 1) for step in steps}
            step = min(steps, key=lambda x: len(steps[x][-1]))

            instructions[0] += step
            for i, s in enumerate(steps[step]):
                instructions[i + 1] += s
    return instructions


def main():
    with open('input.txt') as f:
        data = f.read()

    data = """029A
980A
179A
456A
379A"""

    codes = data.splitlines()
    print(codes)

    # instructions = [quickest_steps(code, 2) for code in codes]
    # print(instructions)
    #
    # complexities = [
    #     (len(instruction[-1]), int(code[:3]))
    #     for instruction, code in zip(instructions, codes)
    # ]
    # print(complexities)
    # print(sum(operator.mul(*complexity) for complexity in complexities))

    instructions = [quickest_steps(code, 2) for code in codes]
    print(instructions)

    complexities = [
        (len(instruction[-1]), int(code[:3]))
        for instruction, code in zip(instructions, codes)
    ]
    print(complexities)
    print(sum(operator.mul(*complexity) for complexity in complexities))


if __name__ == '__main__':
    main()
