def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

#     data = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732""".splitlines()

    data = [list(int(pos) for pos in line) for line in data]

    trail_heads = []

    rows = len(data)
    cols = len(data[0])

    for i, row in enumerate(data):
        for j, pos in enumerate(row):
            if pos == 0:
                trail_heads.append((i, j))

    def create_paths(prev_path):
        paths = []
        i, j, height = prev_path[-1]

        if height == 9:
            return [prev_path]

        # up
        if i > 0:
            next_height = data[i - 1][j]
            if next_height - height == 1:
                paths.extend(create_paths(prev_path + [(i - 1, j, next_height)]))

        # right
        if j < cols - 1:
            next_height = data[i][j + 1]
            if next_height - height == 1:
                paths.extend(create_paths(prev_path + [(i, j + 1, next_height)]))

        # down
        if i < rows - 1:
            next_height = data[i + 1][j]
            if next_height - height == 1:
                paths.extend(create_paths(prev_path + [(i + 1, j, next_height)]))

        # left
        if j > 0:
            next_height = data[i][j - 1]
            if next_height - height == 1:
                paths.extend(create_paths(prev_path + [(i, j - 1, next_height)]))

        return paths

    paths = {}
    scores = {}
    ratings = {}
    for trail_head in trail_heads:
        paths[trail_head] = create_paths([(trail_head[0], trail_head[1], 0)])

        peaks = set()
        for path in paths[trail_head]:
            peaks.add(path[-1])
        scores[trail_head] = len(peaks)

        ratings[trail_head] = len(paths[trail_head])

    print(data)
    print(trail_heads)
    # print(paths)
    # print(scores)

    print(sum(scores.values()))
    print(sum(ratings.values()))


if __name__ == '__main__':
    main()
