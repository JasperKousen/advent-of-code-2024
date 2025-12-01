from collections import Counter

def main():
    with open('input.txt') as f:
        data = f.read()

    testdata = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""

    # data = testdata
    data = data.split('\n\n')

    locks = []
    keys = []

    for entity in data:
        collection = locks if entity[0] == '#' else keys
        entity = entity.splitlines()

        parsed_entity = [-1 for _ in range(5)]
        for line in entity:
            parsed_entity = [p + (e == '#') for p, e in zip(parsed_entity, line)]

        collection.append(parsed_entity)

    print(locks)
    print(keys)

    print(len(locks))
    print(len(keys))

    result = 0
    for lock in locks:
        for key in keys:
            for l, k in zip(lock, key):
                if l + k > 5:
                    break
            else:
                result += 1

    print(result)

if __name__ == '__main__':
    main()