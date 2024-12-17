from collections import Counter
from dataclasses import dataclass
from pprint import pprint


@dataclass
class Robot:
    x: int
    y: int
    horizontal_velocity: int
    vertical_velocity: int

    @property
    def position(self):
        return self.x, self.y

    @property
    def velocity(self):
        return self.horizontal_velocity, self.vertical_velocity

    def move(self, max_x, max_y):
        self.x = (self.x + self.horizontal_velocity) % max_x
        self.y = (self.y + self.vertical_velocity) % max_y


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()
        max_x, max_y = 101, 103

#     data = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3""".splitlines()
#     max_x, max_y = 11, 7

    # data = "p=2,4 v=2,-3".splitlines()

    robots = []
    for line in data:
        p, v = line.split(' ')[0], line.split(' ')[1]

        p = p.split('=')[1].split(',')
        p = tuple(map(int, p))

        v = v.split('=')[1].split(',')
        v = tuple(map(int, v))

        robots.append(Robot(*p, *v))

    CONSECUTIVE_ROBOTS = 6
    for seconds in range(1, 9999):
        for robot in robots:
            robot.move(max_x, max_y)

        counter = Counter(robot.position for robot in robots)

        con = 0
        for y in range(max_y):
            con = 0
            for x in range(max_x):
                if counter[(x, y)]:
                    con += 1
                else:
                    con = 0
                if con >= CONSECUTIVE_ROBOTS:
                    break
            if con >= CONSECUTIVE_ROBOTS:
                break
        if con >= CONSECUTIVE_ROBOTS:
            print(seconds)
            for y in range(max_y):
                for x in range(max_x):
                    if counter[(x, y)]:
                        print(counter[(x, y)], end='')
                    else:
                        print('.', end='')
                print()

            print(' '*max_x)
            print('-'*max_x)
            print(' '*max_x)

    counter = Counter(robot.position for robot in robots)
    print(counter)

    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        if 0 <= robot.x < (max_x - 1) / 2 and 0 <= robot.y < (max_y - 1) / 2:
            q1 += 1
        elif (max_x - 1) / 2 < robot.x <= max_x - 1 and 0 <= robot.y < (max_y - 1) / 2:
            q2 += 1
        elif 0 <= robot.x < (max_x - 1) / 2 and (max_y - 1) / 2 < robot.y <= max_y - 1:
            q3 += 1
        elif (max_x - 1) / 2 < robot.x <= max_x - 1 and (max_y - 1) / 2 < robot.y <= max_y - 1:
            q4 += 1

    pprint(robots)
    print(q1, q2, q3, q4)
    print(q1 * q2 * q3 * q4)

    for y in range(max_y):
        for x in range(max_x):
            if counter[(x, y)]:
                print(counter[(x, y)], end='')
            else:
                print('.', end='')
        print()


if __name__ == '__main__':
    main()
