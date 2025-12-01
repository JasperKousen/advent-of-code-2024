from queue import Queue


def neighbors(x, y, width, height):
    nodes = {
        (max(0, x - 1), y),
        (min(width - 1, x + 1), y),
        (x, max(0, y - 1)),
        (x, min(height - 1, y + 1))
    }
    return {node for node in nodes if node != (x, y)}


def solve(memory):
    height, width = len(memory), len(memory[0])

    nodes = {}
    for y in range(height):
        for x in range(width):
            if memory[y][x] == '.':
                nodes[(x, y)] = {
                    'distance': float('inf'),
                    'previous': None,
                }

    nodes[(0, 0)]['distance'] = 0

    to_visit = Queue()
    to_visit.put((0, 0))

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


def get_path(nodes):
    path = []

    node = (70, 70)
    if nodes[node]['distance'] == float('inf'):
        return path
    path.insert(0, node)

    while nodes[node]['distance']:
        node = nodes[node]['previous']
        path.insert(0, node)

    return path


def print_memory(memory):
    print('\n'.join(''.join(line) for line in memory))


def print_solved_memory(memory, path):
    height, width = len(memory), len(memory[0])

    solved_memory = []
    for y in range(height):
        solved_memory.append([])
        for x in range(width):
            if (x, y) in path:
                solved_memory[y].append('O')
            else:
                solved_memory[y].append(memory[y][x])

    print('\n'.join(''.join(line) for line in solved_memory))


def main():
    with open('input.txt') as file:
        data = file.read().splitlines()
        width, height = 70 + 1, 70 + 1

    #     data = """5,4
    # 4,2
    # 4,5
    # 3,0
    # 2,1
    # 6,3
    # 2,4
    # 1,5
    # 0,6
    # 3,3
    # 2,6
    # 5,1
    # 1,2
    # 5,5
    # 2,5
    # 6,5
    # 1,4
    # 0,4
    # 6,4
    # 1,1
    # 6,1
    # 1,0
    # 0,5
    # 1,6
    # 2,0""".splitlines()
    #     width, height = 7, 7

    data = [tuple(map(int, line.split(','))) for line in data]

    memory = [['.' for _ in range(width)] for _ in range(height)]
    for _, (x, y) in zip(range(1024), data):
        memory[y][x] = '#'

    print_memory(memory)

    nodes = solve(memory)
    node = (70, 70)
    print(nodes[node])

    path = get_path(nodes)
    print(path)

    for x, y in data[1024:]:
        memory[y][x] = '#'

        if (x, y) not in path:
            continue

        nodes = solve(memory)
        path = get_path(nodes)

        if not path:
            print(x, y)
            break


if __name__ == '__main__':
    main()
