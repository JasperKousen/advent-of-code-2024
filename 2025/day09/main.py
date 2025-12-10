from itertools import permutations

def main():
    with open('input.txt') as f:
        data = f.readlines()

    tiles = [tuple(map(int, tile.strip('\n').split(','))) for tile in data]

    rectangles = [
        # abs(tile1[0] - tile2[0]) * abs(tile1[1] - tile2[1])
        (tile1, tile2)
        for tile1, tile2 in permutations(tiles, 2)
    ]

    rectangle_sizes = [
        (abs(tile1[0] - tile2[0]) + 1)
        * (abs(tile1[1] - tile2[1]) + 1)
        for tile1, tile2 in rectangles
    ]

    print(tiles)
    print(len(list(permutations(tiles, 2))))
    # print(rectangles)
    # print(rectangle_sizes)
    print(max(rectangle_sizes))

if __name__ == '__main__':
    main()
