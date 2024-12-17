instruction_pointer = 0
instruction_pointer_jumped = False

REGISTER = {
    'A': 0,
    'B': 0,
    'C': 0,
}


def combo(operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return REGISTER['A']
        case 5:
            return REGISTER['B']
        case 6:
            return REGISTER['C']

    raise ValueError(f'Invalid operand: {operand}')


def operation(opcode):
    match opcode:
        case 0:
            return adv
        case 1:
            return bxl
        case 2:
            return bst
        case 3:
            return jnz
        case 4:
            return bxc
        case 5:
            return out
        case 6:
            return bdv
        case 7:
            return cdv

    raise ValueError(f'Invalid opcode: {opcode}')


def adv(operand):
    REGISTER['A'] = REGISTER['A'] // (2 ** combo(operand))


def bxl(operand):
    REGISTER['B'] = REGISTER['B'] ^ operand


def bst(operand):
    REGISTER['B'] = combo(operand) % 8


def jnz(operand):
    if REGISTER['A'] == 0:
        return

    global instruction_pointer, instruction_pointer_jumped
    INSTRUCTION_POINTER = operand
    INSTRUCTION_POINTER_JUMPED = True


def bxc(operand):
    REGISTER['B'] = REGISTER['B'] ^ REGISTER['C']


def out(operand):
    value = combo(operand) % 8
    for s in str(value):
        print(s + ',', end='')


def bdv(operand):
    REGISTER['B'] = REGISTER['A'] // (2 ** combo(operand))


def cdv(operand):
    REGISTER['C'] = REGISTER['A'] // (2 ** combo(operand))


def main():
    global instruction_pointer, instruction_pointer_jumped
    INSTRUCTION_POINTER = 0

    # REGISTER['A'] = 63281501
    # REGISTER['B'] = 0
    # REGISTER['C'] = 0
    #
    # program = [2, 4, 1, 5, 7, 5, 4, 5, 0, 3, 1, 6, 5, 5, 3, 0]

    REGISTER['A'] = 117440
    REGISTER['B'] = 0
    REGISTER['C'] = 0

    program = [0, 3, 5, 4, 3, 0]

    while INSTRUCTION_POINTER < len(program):
        opcode = program[INSTRUCTION_POINTER]
        operand = program[INSTRUCTION_POINTER + 1]

        op = operation(opcode)
        op(operand)

        if not INSTRUCTION_POINTER_JUMPED:
            INSTRUCTION_POINTER = INSTRUCTION_POINTER + 2
        INSTRUCTION_POINTER_JUMPED = False
    print()
    print(REGISTER)


if __name__ == '__main__':
    main()
