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

    def __repr__(self):
        return f'{self.y}, {self.x} - {self.direction}'

    def step(self, tiles):
        match self.direction:
            case Direction.UP:
                tile_candidate = (self.y - 1, self.x)
                direction_candidate = Direction.RIGHT
            case Direction.RIGHT:
                tile_candidate = (self.y, self.x + 1)
                direction_candidate = Direction.DOWN
            case Direction.DOWN:
                tile_candidate = (self.y + 1, self.x)
                direction_candidate = Direction.LEFT
            case Direction.LEFT:
                tile_candidate = (self.y, self.x - 1)
                direction_candidate = Direction.UP

        # max_y = len(tiles)
        # max_x = len(tiles[0])
        # obstacle_check_y = max(min(tile_candidate[0], max_y - 1), 0)
        # obstacle_check_x = max(min(tile_candidate[1], max_x - 1), 0)

        obstacle_check_y = max(tile_candidate[0], 0)
        obstacle_check_x = max(tile_candidate[1], 0)

        try:
            new_tile_value = tiles[obstacle_check_y][obstacle_check_x]
        except IndexError:
            new_tile_value = None

        if new_tile_value == '#':
            self.direction = direction_candidate
        else:
            self.y, self.x = tile_candidate


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    #         data = """....#.....
    # .........#
    # ..........
    # ..#.......
    # .......#..
    # ..........
    # .#..^.....
    # ........#.
    # #.........
    # ......#...""".splitlines()

    data = [list(line) for line in data]

    for y in range(len(data)):
        try:
            x = data[y].index('^')
            break
        except ValueError:
            continue
    else:
        y, x = None, None

    possible_obstructions = []

    for i in range(len(data)):
        for j in range(len(data[0])):
            # i, j = 6, 3
            if (i, j) == (y, x):
                continue

            if data[i][j] == '#':
                continue

            data[i][j] = '#'

            guard = Guard(y=y, x=x, direction=Direction.UP)

            unique_tiles = set()
            unique_tiles.add((guard.y, guard.x, guard.direction))

            while True:
                guard.step(tiles=data)
                # print((guard.y, guard.x, guard.direction))
                if 0 <= guard.y <= len(data) - 1 and 0 <= guard.x <= len(data[0]) - 1:
                    if (guard.y, guard.x, guard.direction) in unique_tiles:
                        possible_obstructions.append((i, j))
                        print((i, j))
                        break

                    unique_tiles.add((guard.y, guard.x, guard.direction))
                else:
                    break

            data[i][j] = '.'

    print(possible_obstructions)
    print(len(possible_obstructions))


if __name__ == '__main__':
    main()
