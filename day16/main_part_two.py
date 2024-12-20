from queue import Queue


def neighbors(x, y, direction, width, height):
    match direction:
        case 0:
            step = ((min(width - 1, x + 1), y), direction)
        case 90:
            step = ((x, max(0, y - 1)), direction)
        case 180:
            step = ((max(0, x - 1), y), direction)
        case -90:
            step = ((x, min(height - 1, y + 1)), direction)

    nodes = {
        step,
        ((x, y), direction + 90 if direction != 180 else -90),
        ((x, y), direction - 90 if direction != -90 else 180),
    }
    return {node for node in nodes if node != (x, y, direction)}


def solve(maze):
    height, width = len(maze), len(maze[0])

    nodes = {}
    for y in range(height):
        for x in range(width):
            if maze[y][x] in ['.', 'S', 'E']:
                nodes[((x, y), 0)] = {
                    'distance': float('inf'),
                    'previous': set(),
                }
                nodes[((x, y), 90)] = {
                    'distance': float('inf'),
                    'previous': set(),
                }
                nodes[((x, y), 180)] = {
                    'distance': float('inf'),
                    'previous': set(),
                }
                nodes[((x, y), -90)] = {
                    'distance': float('inf'),
                    'previous': set(),
                }

    start = ((1, height - 1 - 1), 0)
    nodes[start]['distance'] = 0

    to_visit = Queue()
    to_visit.put(start)

    while not to_visit.empty():
        node, node_direction = to_visit.get()
        for neighbor, neighbor_direction in neighbors(*node, node_direction, width=width, height=height):
            if maze[neighbor[1]][neighbor[0]] == '#':
                continue

            distance_to_node_from_current = (
                nodes[node, node_direction]['distance']
                + (1 if node_direction == neighbor_direction else 1000)
            )

            # if nodes[(neighbor, neighbor_direction)]['distance'] > distance_to_node_from_current:
            if distance_to_node_from_current < 88468 + 2000:
                if nodes[(neighbor, neighbor_direction)]['distance'] > distance_to_node_from_current:
                    to_visit.put((neighbor, neighbor_direction))
                nodes[(neighbor, neighbor_direction)]['distance'] = min(distance_to_node_from_current,
                                                                        nodes[(neighbor, neighbor_direction)]['distance'])
                nodes[(neighbor, neighbor_direction)]['previous'].add((node, node_direction))
    return nodes


def get_path(nodes, width):
    paths = []

    possible_end_nodes = []
    end_node = (width - 1 - 1, 1)
    for (node, direction) in nodes.keys():
        if node != end_node:
            continue

        if nodes[(node, direction)]['distance'] == float('inf'):
            continue

        possible_end_nodes.append((node, direction))

    if not possible_end_nodes:
        return paths

    node, direction = min(possible_end_nodes, key=lambda node: nodes[node]['distance'])
    cost = nodes[(node, direction)]['distance']
    paths.append([(end_node, direction)])

    def finish_paths(paths):
        new_paths = []
        for path in paths:
            node, direction = path[0]

            previous_nodes = nodes[(node, direction)]['previous']
            distances = {node: nodes[node]['distance'] for node in previous_nodes}
            previous_nodes = [node for node in previous_nodes if distances[node] == min(distances.values())]
            for node, direction in previous_nodes:
                new_paths.append([(node, direction)] + path)

        if all(nodes[path[0]]['distance'] == 0 for path in new_paths):
            return new_paths

        return finish_paths(new_paths)

    paths = finish_paths(paths)

    return paths, cost


def print_maze(maze):
    print('\n'.join(''.join(line) for line in maze))


def print_seen_tiles(maze, tiles):
    height, width = len(maze), len(maze[0])

    solved_maze = []
    for y in range(height):
        solved_maze.append([])
        for x in range(width):
            if (x, y) in tiles:
                solved_maze[y].append('O')
            else:
                solved_maze[y].append(maze[y][x])

    print('\n'.join(''.join(line) for line in solved_maze))


def print_solved_maze(maze, path):
    height, width = len(maze), len(maze[0])

    directions = dict(path)

    solved_maze = []
    for y in range(height):
        solved_maze.append([])
        for x in range(width):
            if (x, y) in directions:
                match directions[(x, y)]:
                    case 0:
                        marker = '>'
                    case 90:
                        marker = '^'
                    case 180:
                        marker = '<'
                    case -90:
                        marker = 'v'
                solved_maze[y].append(marker)
            else:
                solved_maze[y].append(maze[y][x])

    print('\n'.join(''.join(line) for line in solved_maze))


def main():
    with open('input.txt') as file:
        data = file.read()

        data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

    maze = list(map(list, data.splitlines()))

    print_maze(maze)

    nodes = solve(maze)
    paths, cost = get_path(nodes, width=len(maze[0]))
    print(paths)
    print(cost)
    # print_solved_maze(maze, path)

    tiles = {node for path in paths for node, direction in path}
    print(tiles)
    print_seen_tiles(maze, tiles)


if __name__ == '__main__':
    main()
