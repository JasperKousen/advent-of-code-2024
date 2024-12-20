from collections import Counter
from queue import Queue

from tqdm import tqdm


def neighbors(x, y, width, height):
    nodes = {
        (max(0, x - 1), y),
        (min(width - 1, x + 1), y),
        (x, max(0, y - 1)),
        (x, min(height - 1, y + 1))
    }
    return {node for node in nodes if node != (x, y)}


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

    to_visit = Queue()
    to_visit.put(start_node)

    while not to_visit.empty():
        node = to_visit.get()
        for neighbor in neighbors(*node, width=width, height=height):
            if neighbor not in nodes:
                continue
            distance_to_node_from_current = nodes[node]['distance'] + 1

            if nodes[neighbor]['distance'] > distance_to_node_from_current:
                nodes[neighbor]['distance'] = distance_to_node_from_current
                nodes[neighbor]['previous'] = node
                to_visit.put(neighbor)
    return nodes


def get_path(nodes, end_node):
    path = []

    if nodes[end_node]['distance'] == float('inf'):
        return path
    path.insert(0, end_node)

    node = end_node
    while nodes[node]['distance']:
        node = nodes[node]['previous']
        path.insert(0, node)

    return path


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
    print_track(track)

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
    path = get_path(nodes, end_node)
    print_solved_track(track, path)
    base_time = len(path) - 1

    cheat_nodes = []
    for y in range(height):
        for x in range(width):
            if track[y][x] in ['.', 'S', 'E']:
                continue

            if y == height - 1 or x == width - 1:
                continue

            # check left right
            if track[y][x - 1] in ['.', 'S', 'E'] and track[y][x + 1] in ['.', 'S', 'E']:
                cheat_nodes.append((x, y))
                continue

            # check above below
            if track[y - 1][x] in ['.', 'S', 'E'] and track[y + 1][x] in ['.', 'S', 'E']:
                cheat_nodes.append((x, y))
                continue

    counter = Counter()
    counter_100 = 0
    for cheat_node in tqdm(cheat_nodes):
        nodes = solve(track, start_node, cheat_node=cheat_node)
        path = get_path(nodes, end_node)
        cheated_time = len(path) - 1
        counter.update([base_time - cheated_time])

        counter_100 += base_time - cheated_time >= 100

    print(sorted(counter.items(), key=lambda c: c[0], reverse=False))
    print(counter_100)



if __name__ == '__main__':
    main()
