def neighbors(x, y, width, height):
    neighbors = set()

    if x > 0:
        neighbors.add((x - 1, y))
    if x < width - 1:
        neighbors.add((x + 1, y))
    if y > 0:
        neighbors.add((x, y - 1))
    if y < height - 1:
        neighbors.add((x, y + 1))

    return neighbors


def naive_neighbors(x, y):
    return {
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    }


def naive_neighbors_with_direction(x, y):
    return {
        ((x - 1, y), '<'),
        ((x + 1, y), '>'),
        ((x, y - 1), '^'),
        ((x, y + 1), 'v'),
    }


def side_neighbors(x, y, direction):
    match direction:
        case '^' | 'v':
            return {
                ((x - 1, y), direction),
                ((x + 1, y), direction),
            }
        case '<' | '>':
            return {
                ((x, y - 1), direction),
                ((x, y + 1), direction),
            }
        case _:
            raise ValueError


def find_regions(garden):
    height, width = len(garden), len(garden[0])

    regions = list()
    seen = set()

    for y in range(height):
        for x in range(width):
            if (x, y) in seen:
                continue

            new_region = [(x, y)]
            seen.add((x, y))
            to_check = neighbors(x, y, width, height)

            while to_check:
                neighbor = to_check.pop()

                if neighbor in seen:
                    continue

                if garden[y][x] != garden[neighbor[1]][neighbor[0]]:
                    continue

                new_region.append(neighbor)
                seen.add(neighbor)
                to_check.update(neighbors(*neighbor, width, height))

            regions.append(new_region)

    return regions


def get_perimeter(region):
    perimeter = 0
    for plot in region:
        perimeter += 4 - sum(neighbor in region for neighbor in naive_neighbors(*plot))
    return perimeter


def get_sides(region):
    plot_sides = set()
    for plot in region:
        plot_sides.update({
            neighbor for neighbor in naive_neighbors_with_direction(*plot)
            if neighbor[0] not in region
        })

    sides = []
    seen = set()
    for (x, y), direction in plot_sides:
        if ((x, y), direction) in seen:
            continue

        new_side = [((x, y), direction)]
        to_check = side_neighbors(x, y, direction)

        while to_check:
            side_neighbor = to_check.pop()

            if side_neighbor in seen:
                continue

            if side_neighbor not in plot_sides:
                continue

            new_side.append(side_neighbor)
            seen.add(side_neighbor)
            to_check.update(side_neighbors(*side_neighbor[0], side_neighbor[1]))

        sides.append(new_side)

    return sides


def main():
    with open('input.txt') as f:
        data = f.read()

#     data = """AAAA
# BBCD
# BBCC
# EEEC"""
#
#     data = """OOOOO
# OXOXO
# OOOOO
# OXOXO
# OOOOO"""
#
#     data = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""

#     data = """EEEEE
# EXXXX
# EEEEE
# EXXXX
# EEEEE"""
#
#     data = """AAAAAA
# AAABBA
# AAABBA
# ABBAAA
# ABBAAA
# AAAAAA"""

    garden = list(map(list, data.splitlines()))
    regions = find_regions(garden)
    print(regions)

    perimeters = {tuple(region): get_perimeter(region) for region in regions}
    print(perimeters)

    costs = sum(
        len(region) * perimeters[tuple(region)]
        for region in regions
    )
    print(costs)

    sides = {tuple(region): len(get_sides(region)) for region in regions}
    print(sides)

    costs = sum(
        len(region) * sides[tuple(region)]
        for region in regions
    )
    print(costs)


if __name__ == '__main__':
    main()
