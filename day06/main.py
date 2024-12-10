from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class Guard:
    def __init__(self, y, x, direction):
        self.y = y
        self.x = x
        self.direction = direction

    def step(self, tiles):
        match self.direction:
            case Direction.UP:
                tile_candidate = (self.y - 1, self.x)
                possible_new_direction = Direction.RIGHT
            case Direction.RIGHT:
                tile_candidate = (self.y, self.x + 1)
                possible_new_direction = Direction.DOWN
            case Direction.DOWN:
                tile_candidate = (self.y + 1, self.x)
                possible_new_direction = Direction.LEFT
            case Direction.LEFT:
                tile_candidate = (self.y, self.x - 1)
                possible_new_direction = Direction.UP

        try:
            new_tile_value = tiles[tile_candidate[0]][tile_candidate[1]]
        except IndexError:
            new_tile_value = None

        if new_tile_value == '#':
            self.direction = possible_new_direction
            return self.step(tiles)

        self.y, self.x = tile_candidate
        return tile_candidate


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()

    for y in range(len(data)):
        try:
            x = data[y].index('^')
            break
        except ValueError:
            continue
    else:
        y, x = None, None

    guard = Guard(y=y, x=x, direction=Direction.UP)

    unique_tiles = set()
    unique_tiles.add((guard.y, guard.x))

    while True:
        tile = guard.step(tiles=data)
        if 0 <= tile[0] <= len(data) - 1 and 0 <= tile[1] <= len(data[0]) - 1:
            unique_tiles.add(tile)
        else:
            break

    print(unique_tiles)
    print(len(unique_tiles))


if __name__ == '__main__':
    main()
