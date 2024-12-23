from collections import defaultdict
from pprint import pprint

from tqdm import tqdm

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

    seen = set()

    def find_networks(computer, network):
        network = network.union(set([computer]))
        networks = set()

        network_tuple = tuple(sorted(network))
        if network_tuple in seen:
            return networks
        seen.add(network_tuple)

        connected_computers = computers[computer]
        for new_computer in connected_computers - network:
            if not network.issubset(computers[new_computer]):
                continue

            networks.update(find_networks(new_computer, network))

        if not networks:
            networks.add(tuple(sorted(network)))

        return networks

    networks = set()
    for computer, connected_computers in tqdm(computers.items()):
        new_networks = find_networks(computer, network=set())
        networks.update(new_networks)

    pprint(','.join(max(networks, key=len)))


if __name__ == '__main__':
    main()
