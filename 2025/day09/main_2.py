from itertools import permutations

import matplotlib.pyplot as plt


def main():
    with open('input.txt') as f:
        data = f.readlines()

    tiles = [tuple(map(int, tile.strip('\n').split(','))) for tile in data]

    fig, ax = plt.subplots()
    for i, tile in enumerate(tiles):
        prev_tile = tiles[i - 1]
        ax.plot(
            [prev_tile[0], tile[0]],
            [prev_tile[1], tile[1]],
            'r.-',
        )

    ax.add_patch(plt.Rectangle(
        (5069, 50422),
        width=(abs(94525 - 5069) + 1),
        height=(abs(50422 - 66396) + 1),
        linewidth=1,
        color='blue',
    ))
    # plt.ylim([30_000, 50_000])
    # plt.ylim([50_000, 69_000])
    plt.show()

    # 94525, 50422 -> 94816,66941 -> 5069,66396
    # 94525, 48322 -> 94082,32608 -> 5256,32944

    print(
        (abs(94525 - 5069) + 1)
        * (abs(50422 - 66396) + 1),
    )
    print(
        (abs(94525 - 5256) + 1)
        * (abs(48322 - 32944) + 1),
    )


if __name__ == '__main__':
    main()
