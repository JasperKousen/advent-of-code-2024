import operator
from pprint import pprint

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

priority = {
    '>': 0,
    '^': 1,
    'v': 2,
    '<': 3,
}

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


def instructions_keypad(code, coordinate_function):
    code = 'A' + code

    instructions = ''
    for from_button, to_button in zip(code, code[1:]):
        from_coordinates, to_coordinates = coordinate_function(from_button), coordinate_function(to_button)

        instruction = ''
        # left right
        if to_coordinates[1] < from_coordinates[1]:
            step = '<'
        else:
            step = '>'
        instruction += step * abs(to_coordinates[1] - from_coordinates[1])

        # up down
        if to_coordinates[0] < from_coordinates[0]:
            step = 'v'
        else:
            step = '^'
        instruction += step * abs(to_coordinates[0] - from_coordinates[0])

        instructions += ''.join(sorted(instruction, key=lambda x: priority[x])) + 'A'
    return instructions


def instructions_numeric_keypad(code):
    return instructions_keypad(code, numeric_keypad_coordinates)


def instructions_directional_keypad(code):
    return instructions_keypad(code, directional_keypad_coordinates)


def main():
    with open('input.txt') as f:
        data = f.read()

    data = """029A
980A
179A
456A
379A"""

    # codes = list(map(list, data.splitlines()))
    codes = data.splitlines()
    print(codes)

    instructions_1 = [instructions_numeric_keypad(code) for code in codes]
    instructions_2 = [instructions_directional_keypad(code) for code in instructions_1]
    instructions_3 = [instructions_directional_keypad(code) for code in instructions_2]

    pprint(list(zip(codes, instructions_1, instructions_2, instructions_3)))

    complexities = [
        (len(instruction), int(code[:3]))
        for instruction, code in zip(instructions_3, codes)
    ]
    print(complexities)
    print(sum(operator.mul(*complexity) for complexity in complexities))


if __name__ == '__main__':
    main()
