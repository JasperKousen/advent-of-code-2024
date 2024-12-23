from collections import defaultdict
from pprint import pprint

def main():
    with open('input.txt') as f:
        data = f.read()

#     data = """kh-tc
# qp-kh
# de-cg
# ka-co
# yn-aq
# qp-ub
# cg-tb
# vc-aq
# tb-ka
# wh-tc
# yn-cg
# kh-ub
# ta-co
# de-co
# tc-td
# tb-wq
# wh-td
# ta-ka
# td-qp
# aq-cg
# wq-ub
# ub-vc
# de-ta
# wq-aq
# wq-vc
# wh-yn
# ka-de
# kh-ta
# co-tc
# wh-qp
# tb-vc
# td-yn"""

    connections = data.splitlines()

    computers = defaultdict(set)
    for connection in connections:
        computer_1, computer_2 = tuple(connection.split('-'))

        computers[computer_1].add(computer_2)
        computers[computer_2].add(computer_1)

    print(computers)

    networks = set()
    networks_with_t = set()
    for computer_1, connected_computers_1 in computers.items():
        for computer_2 in connected_computers_1:
            connected_computers_2 = computers[computer_2]
            for computer_3 in connected_computers_1.intersection(connected_computers_2):
                network = tuple(sorted([computer_1, computer_2, computer_3]))

                networks.add(network)
                if any(c.startswith('t') for c in network):
                    networks_with_t.add(network)

    pprint(networks)
    pprint(networks_with_t)
    print(len(networks_with_t))


if __name__ == '__main__':
    main()
