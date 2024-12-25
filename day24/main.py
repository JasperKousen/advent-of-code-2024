import itertools
import time
from operator import and_, or_, xor
from pprint import pprint

def get_operator(operation):
    match operation:
        case 'AND':
            return and_
        case 'OR':
            return or_
        case 'XOR':
            return xor


def main():
    with open('input.txt') as f:
        data = f.read()

#     data = """x00: 1
# x01: 1
# x02: 1
# y00: 0
# y01: 1
# y02: 0
#
# x00 AND y00 -> z00
# x01 XOR y01 -> z01
# x02 OR y02 -> z02"""
#
#     data = """x00: 1
# x01: 0
# x02: 1
# x03: 1
# x04: 0
# y00: 1
# y01: 1
# y02: 1
# y03: 1
# y04: 1
#
# ntg XOR fgs -> mjb
# y02 OR x01 -> tnw
# kwq OR kpj -> z05
# x00 OR x03 -> fst
# tgd XOR rvg -> z01
# vdt OR tnw -> bfw
# bfw AND frj -> z10
# ffh OR nrd -> bqk
# y00 AND y03 -> djm
# y03 OR y00 -> psh
# bqk OR frj -> z08
# tnw OR fst -> frj
# gnj AND tgd -> z11
# bfw XOR mjb -> z00
# x03 OR x00 -> vdt
# gnj AND wpb -> z02
# x04 AND y00 -> kjc
# djm OR pbm -> qhw
# nrd AND vdt -> hwm
# kjc AND fst -> rvg
# y04 OR y02 -> fgs
# y01 AND x02 -> pbm
# ntg OR kjc -> kwq
# psh XOR fgs -> tgd
# qhw XOR tgd -> z09
# pbm OR djm -> kpj
# x03 XOR y03 -> ffh
# x00 XOR y04 -> ntg
# bfw OR bqk -> z06
# nrd XOR fgs -> wpb
# frj XOR qhw -> z04
# bqk OR frj -> z07
# y03 OR x01 -> nrd
# hwm AND bqk -> z03
# tgd XOR rvg -> z12
# tnw OR pbm -> gnj"""

    data = data.split('\n\n')

    wires = data[0].splitlines()
    wires = [wire.split(': ') for wire in wires]
    wires = {wire[0]: int(wire[1]) for wire in wires}

    gates = data[1].splitlines()
    gates = [tuple(gate.split(' ')) for gate in gates]
    # gates = [(input_1, get_operator(operation), input_2, '->', output) for input_1, operation, input_2, _, output in gates]
    gates = [(tuple(sorted([input_1, input_2])), operation, output) for input_1, operation, input_2, _, output in gates]

    s = time.perf_counter()
    queue = gates.copy()
    while queue:
        (input_1, input_2), operation, output = queue.pop(0)
        if input_1 not in wires or input_2 not in wires:
            queue.append(((input_1, input_2), operation, output))
            continue

        wires[output] = get_operator(operation)(wires[input_1], wires[input_2])

    z_bits = [str(value) for wire, value in sorted(wires.items()) if wire.startswith('z')]
    e = time.perf_counter()
    print(''.join(reversed(z_bits)))
    print(int(''.join(reversed(z_bits)), 2))

    print(e-s)
    # gate_swaps = list(itertools.combinations(gates, r=8))
    # print(gate_swaps)
    # print(len(gate_swaps))

    print(len(gates))

    print({gate for gate in gates if gate[0][0] == 'x00' or gate[0][1] == 'x00'})
    print({gate for gate in gates if gate[0][0] == 'y00' or gate[0][1] == 'y00'})

    print('-------------')

    print({gate for gate in gates if gate[0][0] == 'x01' or gate[0][1] == 'x01'})
    print({gate for gate in gates if gate[0][0] == 'y01' or gate[0][1] == 'y01'})
    print({gate for gate in gates if gate[0][0] == 'rvb' or gate[0][1] == 'rvb'})
    print('qkm: remainder from previous -- XOR(qkm, rvb := XOR(x01, y01)) -> z01')
    print({gate for gate in gates if gate[0] == 'svq' or gate[2] == 'svq'})
    print('qfj: remainder?')

    print('-------------')

    print({gate for gate in gates if gate[0][1] == 'x02' or gate[0][1] == 'x02'})
    print({gate for gate in gates if gate[0][1] == 'y02' or gate[0][1] == 'y02'})
    print({gate for gate in gates if gate[0][1] == 'hvf' or gate[0][1] == 'hvf'})
    print('qfj: remainder from previous -- XOR(qkj, hvf := XOR(x02, y02)) -> z02')
    print({gate for gate in gates if gate[0][1] == 'nps' or gate[0][1] == 'nps'})
    print('kgk: remainder?')

    print('-------------')
    print({gate for gate in gates if gate[2] == 'z45'})

    # sorted_gates = []
    # for input_1, operation, input_2, _, output in gates:
    #     inputs = sorted([input_1, input_2])
    #
    #     sorted_gates.append((inputs[0], operation, inputs[1], '->', output))
    # sorted_gates = sorted(sorted_gates, key=lambda gate: (gate[0], gate[2]))
    # print(sorted_gates)

    gates.remove((('ctg', 'rjm'), 'XOR', 'qnw'))
    gates.remove((('dnn', 'mrm'), 'OR', 'z15'))
    gates.append((('ctg', 'rjm'), 'XOR', 'z15'))
    gates.append((('dnn', 'mrm'), 'OR', 'qnw'))

    gates.remove((('x20', 'y20'), 'AND', 'z20'))
    gates.remove((('msn', 'wrb'), 'XOR', 'cqr'))
    gates.append((('x20', 'y20'), 'AND', 'cqr'))
    gates.append((('msn', 'wrb'), 'XOR', 'z20'))

    gates.remove((('x27', 'y27'), 'XOR', 'ncd'))
    gates.remove((('x27', 'y27'), 'AND', 'nfj'))
    gates.append((('x27', 'y27'), 'XOR', 'nfj'))
    gates.append((('x27', 'y27'), 'AND', 'ncd'))

    gates.remove((('dnt', 'fcm'), 'XOR', 'vkg'))
    gates.remove((('dnt', 'fcm'), 'AND', 'z37'))
    gates.append((('dnt', 'fcm'), 'XOR', 'z37'))
    gates.append((('dnt', 'fcm'), 'AND', 'vkg'))

    previous_remainder = 'qkm'
    for i in range(1, 44):
        print(i)
        x_xor_y = next(gate for gate in gates if gate[1] == 'XOR' and f'y{i:0>2}' in gate[0])
        x_and_y = next(gate for gate in gates if gate[1] == 'AND' and f'y{i:0>2}' in gate[0])

        print(x_xor_y, x_and_y)

        # check output xor has xor with previous remainder and output zi
        xor_with_remainder = [gate for gate in gates if gate[1] == 'XOR' and gate[0] == tuple(sorted([previous_remainder, x_xor_y[2]]))]

        if not xor_with_remainder:
            print(f'{i} - No XOR with previous remainder')
            z = f'z{i:0>2}'
            print(f'{i} - {[gate for gate in gates if gate[1] == "XOR" and gate[2] == z]}')
        else:
            xor_with_remainder = xor_with_remainder[0]
            print(xor_with_remainder)

            if xor_with_remainder[2] != f'z{i:0>2}':
                print(f'{i} - XOR with previous remainder not correct output, should be "z{i:0>2}"')

        # check output xor has and with previous remainder which has or with and
        and_with_remainder = [gate for gate in gates if gate[1] == 'AND' and gate[0] == tuple(sorted([previous_remainder, x_xor_y[2]]))]

        if not and_with_remainder:
            print(f'{i} - No AND with previous remainder')
            print(f'{i} - {[gate for gate in gates if gate[1] == "AND" and previous_remainder in gate[0]]}')
            print(f'{i} - {[gate for gate in gates if gate[1] == "AND" and x_xor_y[2] in gate[0]]}')
            continue
        and_with_remainder = and_with_remainder[0]
        print(and_with_remainder)

        remainder_or = [gate for gate in gates if gate[1] == 'OR' and gate[0] == tuple(sorted([and_with_remainder[2], x_and_y[2]]))]

        if not remainder_or:
            print(f'{i} - No remainder OR')
            continue
        remainder_or = remainder_or[0]
        print(remainder_or)

        previous_remainder = remainder_or[2]

    print(','.join(sorted(['qnw', 'z15', 'z20', 'cqr', 'ncd', 'nfj', 'vkg', 'z37'])))

if __name__ == '__main__':
    main()
