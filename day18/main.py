from queue import Queue

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

    print('\n'.join(''.join(line) for line in memory))

    def neighbors(x, y):
        nodes = {
            (max(0, x - 1), y),
            (min(width - 1, x + 1), y),
            (x, max(0, y - 1)),
            (x, min(height - 1, y + 1))
        }
        return {node for node in nodes if node != (x, y)}

    nodes = {}
    unvisited = []
    for y in range(height):
        for x in range(width):
            if memory[y][x] == '.':
                nodes[(x, y)] = {
                    'distance': float('inf'),
                    'previous': None,
                }
                unvisited.append((x, y))

    nodes[(0, 0)]['distance'] = 0
    unvisited.remove((0, 0))

    to_visit = Queue()
    to_visit.put((0, 0))

    while not to_visit.empty():
        node = to_visit.get()
        for neighbor in neighbors(*node):
            if neighbor not in nodes:
                continue
            distance_to_node_from_current = nodes[node]['distance'] + 1

            if nodes[neighbor]['distance'] > distance_to_node_from_current:
                nodes[neighbor]['distance'] = distance_to_node_from_current
                nodes[neighbor]['previous'] = node
                to_visit.put(neighbor)

    solved_memory = []
    for y in range(height):
        solved_memory.append([])
        for x in range(width):
            if memory[y][x] == '.':
                solved_memory[y].append(nodes[(x, y)]['distance'])
            else:
                solved_memory[y].append('#')

    print('\n'.join(''.join(str(n)[-1] for n in line) for line in solved_memory))
    print(nodes[(70, 70)])

if __name__ == '__main__':
    main()
