import copy
from collections import Counter
from pprint import pprint

from tqdm import tqdm


def neighbors(x, y, width, height):
    nodes = set()

    if x > 0:
        nodes.add((x - 1, y))
    if x < width - 1:
        nodes.add((x + 1, y))
    if y > 0:
        nodes.add((x, y - 1))
    if y < height - 1:
        nodes.add((x, y + 1))

    return nodes


def solve(track, start_node, cheat_node=None):
    height, width = len(track), len(track[0])

    nodes = {}
    for y in range(height):
        for x in range(width):
            if track[y][x] in ['.', 'S', 'E'] or (x, y) == cheat_node:
                nodes[(x, y)] = {
                    'distance': float('inf'),
                    'previous': None,
                }

    nodes[start_node]['distance'] = 0

    to_visit = [start_node]
    while to_visit:
        node = to_visit.pop(0)
        for neighbor in neighbors(*node, width=width, height=height):
            if neighbor not in nodes:
                continue
            distance_to_node_from_current = nodes[node]['distance'] + 1

            if nodes[neighbor]['distance'] > distance_to_node_from_current:
                nodes[neighbor]['distance'] = distance_to_node_from_current
                nodes[neighbor]['previous'] = node
                to_visit.append(neighbor)
    return nodes


def solve_with_cheat(track, nodes, cheat_start, cheat_end):
    height, width = len(track), len(track[0])

    nodes = copy.deepcopy(nodes)
    to_visit = set()

    distance_cheat_start_to_end = (
        nodes[cheat_start]['distance']
        + abs(cheat_start[0] - cheat_end[0]) + abs(cheat_start[1] - cheat_end[1])
    )

    if nodes[cheat_end]['distance'] > distance_cheat_start_to_end:
        nodes[cheat_end]['distance'] = distance_cheat_start_to_end
        nodes[cheat_end]['previous'] = cheat_start
        to_visit.add(cheat_end)

    while to_visit:
        node = to_visit.pop()
        for neighbor in neighbors(*node, width=width, height=height):
            if neighbor not in nodes:
                continue
            distance_to_node_from_current = nodes[node]['distance'] + 1

            if nodes[neighbor]['distance'] > distance_to_node_from_current:
                nodes[neighbor]['distance'] = distance_to_node_from_current
                nodes[neighbor]['previous'] = node
                to_visit.add(neighbor)

    return nodes

def cheat_difference(nodes, cheat_start, cheat_end):
    distance_cheat_start_to_end = (
        nodes[cheat_start]['distance']
        + abs(cheat_start[0] - cheat_end[0]) + abs(cheat_start[1] - cheat_end[1])
    )

    return nodes[cheat_end]['distance'] - distance_cheat_start_to_end


def get_path(nodes, end_node):
    path = []

    if nodes[end_node]['distance'] == float('inf'):
        return path, -1
    path.append(end_node)

    node = end_node
    while nodes[node]['distance']:
        node = nodes[node]['previous']
        path.append(node)

    return list(reversed(path)), nodes[end_node]['distance']


def print_track(track):
    print('\n'.join(''.join(line) for line in track))


def print_solved_track(track, path):
    height, width = len(track), len(track[0])

    solved_track = []
    for y in range(height):
        solved_track.append([])
        for x in range(width):
            if (x, y) in path:
                solved_track[y].append('O')
            else:
                solved_track[y].append(track[y][x])

    print('\n'.join(''.join(line) for line in solved_track))


def main():
    with open('input.txt') as f:
        data = f.read()

#     data = """###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############"""

    track = list(map(list, data.splitlines()))
    # print_track(track)

    height, width = len(track), len(track[0])

    start_node, end_node = None, None
    for y in range(height):
        for x in range(width):
            match track[y][x]:
                case 'S':
                    start_node = (x, y)
                case 'E':
                    end_node = (x, y)

    nodes = solve(track, start_node)
    path, base_time = get_path(nodes, end_node)
    # print_solved_track(track, path)

    # cheated_nodes = solve_with_cheat(track, nodes, cheat_start=(1, 3), cheat_end=(3, 7))
    # cheated_path, cheated_time = get_path(cheated_nodes, end_node)
    # print_solved_track(track, cheated_path)
    # print(cheated_time)
    # print(base_time - cheated_time)
    # print(cheat_difference(nodes, cheat_start=(1, 3), cheat_end=(3, 7)))
    #
    # cheated_nodes = solve_with_cheat(track, nodes, cheat_start=(7, 1), cheat_end=(9, 1))
    # cheated_path, cheated_time = get_path(cheated_nodes, end_node)
    # print_solved_track(track, cheated_path)
    # print(cheated_time)
    # print(base_time - cheated_time)
    # print(cheat_difference(nodes, cheat_start=(7, 1), cheat_end=(9, 1)))

    cheats = set()
    for y in range(height):
        for x in range(width):
            if track[y][x] not in ['.', 'S', 'E']:
                continue

            if y == 0 or y == height - 1 or x == 0 or x == width - 1:
                continue

            if all([
                track[y][x - 1] == '#',
                track[y][x + 1] == '#',
                track[y - 1][x] == '#',
                track[y + 1][x] == '#',
            ]):
                continue

            cheat_start = (x, y)
            for i in range(-20, 21):
                for j in range(-20, 21):
                    if abs(i) + abs(j) > 20:
                        continue

                    cheat_end = (
                        min(max(x + i, 0), width - 1),
                        min(max(y + j, 0), height - 1)
                    )

                    if track[cheat_end[1]][cheat_end[0]] != '#':
                        cheats.add((cheat_start, cheat_end))

    counter = Counter()
    counter_100 = 0
    for cheat_start, cheat_end in tqdm(cheats):
        cheated_decrease = cheat_difference(nodes, cheat_start, cheat_end)
        counter.update([cheated_decrease])

        counter_100 += cheated_decrease >= 100

    print(counter)
    # pprint(dict(sorted(counter.items(), key=lambda c: c[0], reverse=False)))
    # pprint(dict(sorted([(x, count) for x, count in counter.items() if x >= 50])))
    print(counter_100)


if __name__ == '__main__':
    # import cProfile
    #
    # cProfile.run('main()', 'stats')
    #
    # import pstats
    #
    # p = pstats.Stats('stats')
    # p.strip_dirs().sort_stats('tottime').print_stats()
    main()
