import itertools
from dataclasses import dataclass


@dataclass
class Robot:
    x: int
    y: int

    @property
    def position(self):
        return self.x, self.y

    def move(self, direction, board):
        height = len(board)
        width = len(board[0])

        def positions(x, y, direction):
            match direction:
                case '^':
                    return zip(itertools.repeat(x), range(y - 1, 0 - 1, -1))
                case '>':
                    return zip(range(x + 1, width), itertools.repeat(y))
                case 'v':
                    return zip(itertools.repeat(x), range(y + 1, height, 1))
                case '<':
                    return zip(range(x - 1, 0 - 1, -1), itertools.repeat(y))

        def find_move(x, y, direction):
            boxes = set()
            next_positions = list(positions(x, y, direction))
            if not next_positions:
                return False, []
            for x, y in positions(x, y, direction):
                match board[y][x]:
                    case '.':
                        return True, boxes
                    case '[' | ']' as edge:
                        if edge == '[':
                            boxes.add((x, y))
                            offset = 1
                        else:
                            boxes.add((x - 1, y))
                            offset = -1

                        match direction:
                            case '>' | '<':
                                continue
                            case '^' | 'v':
                                move_is_possible, extra_boxes = find_move(x, y, direction)
                                if not move_is_possible:
                                    return False, []
                                boxes.update(extra_boxes)

                                move_is_possible, extra_boxes = find_move(x + offset, y, direction)
                                if not move_is_possible:
                                    return False, []
                                boxes.update(extra_boxes)
                    case '#':
                        return False, []
            return True, boxes

        move_is_possible, boxes = find_move(x=self.x, y=self.y, direction=direction)

        if not move_is_possible:
            return

        # delete boxes
        for x, y in boxes:
            board[y][x] = '.'
            board[y][x+1] = '.'

        # redraw boxes
        for x, y in boxes:
            match direction:
                case '^':
                    board[y - 1][x] = '['
                    board[y - 1][x + 1] = ']'
                case '>':
                    board[y][x + 1] = '['
                    board[y][x + 2] = ']'
                case 'v':
                    board[y + 1][x] = '['
                    board[y + 1][x + 1] = ']'
                case '<':
                    board[y][x - 1] = '['
                    board[y][x] = ']'

        match direction:
            case '^':
                board[self.y][self.x] = '.'
                self.y -= 1
                board[self.y][self.x] = '@'
            case '>':
                board[self.y][self.x] = '.'
                self.x += 1
                board[self.y][self.x] = '@'
            case 'v':
                board[self.y][self.x] = '.'
                self.y += 1
                board[self.y][self.x] = '@'
            case '<':
                board[self.y][self.x] = '.'
                self.x -= 1
                board[self.y][self.x] = '@'


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

#     data = """#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######
#
# <vv<<^^<<^^""".splitlines()
#
#     data = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########
#
# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""".splitlines()

    board = list(map(list, data))
    moves = []

    while line := board.pop(-1):
        moves[0:0] = line

    new_board = []
    for row in board:
        new_row = []
        for tile in row:
            match tile:
                case '#':
                    new_row.append('#')
                    new_row.append('#')
                case 'O':
                    new_row.append('[')
                    new_row.append(']')
                case '.':
                    new_row.append('.')
                    new_row.append('.')
                case '@':
                    new_row.append('@')
                    new_row.append('.')

        new_board.append(new_row)
    board = new_board

    height = len(board)
    width = len(board[0])

    print('\n'.join(''.join(line) for line in board))
    print('_' * width)

    for y in range(height):
        for x in range(width):
            if board[y][x] == '@':
                robot = Robot(x=x, y=y)

    for move in moves:
        print(move)
        robot.move(direction=move, board=board)
        print('\n'.join(''.join(line) for line in board))
        print('_' * width)

    # result = 0
    # for y in range(height):
    #     for x in range(width):
    #         if board[y][x] == '[':
    #             GPS_y = min(y, height - 1 - y)
    #             GPS_x = min(x, width - 1 - (x + 1))
    #             result += 100 * GPS_y + GPS_x
    # print(result)

    result = 0
    for y in range(height):
        for x in range(width):
            if board[y][x] == '[':
                result += 100 * y + x
    print(result)


if __name__ == '__main__':
    main()
