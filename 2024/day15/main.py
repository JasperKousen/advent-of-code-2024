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

        boxes = []
        match direction:
            case '^':
                for y in range(self.y - 1, 0 - 1, -1):
                    match board[y][self.x]:
                        case '.':
                            break
                        case 'O':
                            boxes.append((self.x, y))
                        case '#':
                            return
                board[self.y][self.x] = '.'
                self.y -= 1
                board[self.y][self.x] = '@'
                if boxes:
                    x, y = boxes[-1]
                    board[y - 1][x] = 'O'
            case '>':
                for x in range(self.x + 1, width):
                    match board[self.y][x]:
                        case '.':
                            break
                        case 'O':
                            boxes.append((x, self.y))
                        case '#':
                            return
                board[self.y][self.x] = '.'
                self.x += 1
                board[self.y][self.x] = '@'
                if boxes:
                    x, y = boxes[-1]
                    board[y][x + 1] = 'O'
            case 'v':
                for y in range(self.y + 1, height, 1):
                    match board[y][self.x]:
                        case '.':
                            break
                        case 'O':
                            boxes.append((self.x, y))
                        case '#':
                            return
                board[self.y][self.x] = '.'
                self.y += 1
                board[self.y][self.x] = '@'
                if boxes:
                    x, y = boxes[-1]
                    board[y + 1][x] = 'O'
            case '<':
                for x in range(self.x - 1, 0 - 1, -1):
                    match board[self.y][x]:
                        case '.':
                            break
                        case 'O':
                            boxes.append((x, self.y))
                        case '#':
                            return
                board[self.y][self.x] = '.'
                self.x -= 1
                board[self.y][self.x] = '@'
                if boxes:
                    x, y = boxes[-1]
                    board[y][x - 1] = 'O'


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

#     data = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########
#
# <^^>>>vv<v>>v<<""".splitlines()
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

    height = len(board)
    width = len(board[0])

    for y in range(height):
        for x in range(width):
            if board[y][x] == '@':
                robot = Robot(x=x, y=y)

    print('\n'.join(''.join(line) for line in board))
    print('_' * width)
    for move in moves:
        print(move)
        robot.move(direction=move, board=board)
        print('\n'.join(''.join(line) for line in board))
        print('_' * width)

    result = 0
    for y in range(height):
        for x in range(width):
            if board[y][x] == 'O':
                result += 100 * y + x
    print(result)


if __name__ == '__main__':
    main()
