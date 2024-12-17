import itertools


def run(program, a=0, b=0, c=0, verbose=False):
    instruction_pointer = 0
    instruction_pointer_jumped = False

    REGISTER = {
        'A': a,
        'B': b,
        'C': c,
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

    while instruction_pointer < len(program):

        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        match opcode:
            case 0:
                REGISTER['A'] = REGISTER['A'] // (2 ** combo(operand))
            case 1:
                REGISTER['B'] = REGISTER['B'] ^ operand
            case 2:
                REGISTER['B'] = combo(operand) % 8
            case 3:
                if REGISTER['A'] != 0:
                    instruction_pointer = operand
                    instruction_pointer_jumped = True
            case 4:
                REGISTER['B'] = REGISTER['B'] ^ REGISTER['C']
            case 5:
                value = combo(operand) % 8
                if verbose:
                    print(value, REGISTER)
                for s in str(value):
                    yield int(s)
            case 6:
                REGISTER['B'] = REGISTER['A'] // (2 ** combo(operand))
            case 7:
                REGISTER['C'] = REGISTER['A'] // (2 ** combo(operand))

        if not instruction_pointer_jumped:
            instruction_pointer = instruction_pointer + 2
        instruction_pointer_jumped = False

    # print(','.join(output))
    # print(REGISTER)
    return


def main():
    # program = [2, 4, 1, 5, 7, 5, 4, 5, 0, 3, 1, 6, 5, 5, 3, 0]
    program = [
        2, 4,  # B = A % 8
        1, 5,  # B = B XOR 5
        7, 5,  # C = A // 2^B
        4, 5,  # B = B XOR C
        0, 3,  # A = A // 8
        1, 6,  # B = B XOR 6
        5, 5,  # print B % 8
        3, 0   # GOTO 00
    ]

    # print(list(run(program=program, a=279_474_976_710_655, verbose=False)))
    # for a in range(8**12 + 4, 8**12 + 5 * 8**12 + 1, 8**12):
    for a in range(105689481478144, 105759274696704 + 1, 1):
        # 105544526331904 , 114349209288704
        # 127534758887424 , 131941395333120
        # 136330851909632 , 140737488355328

        # print(a, list(run(program=program, a=a, verbose=False)))
        # print(a)
        output = run(program=program, a=a)

        for o, p in itertools.zip_longest(output, program):
            if o is None or p is None or o != p:
                break
        else:
            print(program, a)
            return


if __name__ == '__main__':
    main()
