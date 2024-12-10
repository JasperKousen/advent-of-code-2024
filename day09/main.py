def main():
    with open('input.txt') as f:
        data = f.read()

    # data = '2333133121414131402'

    data = data.rstrip()

    files = data[0::2]
    spaces = data[1::2] + '0'

    id = 0
    blocks = []
    for file, space in zip(files, spaces):
        blocks += [id] * int(file)
        blocks += ['.'] * int(space)
        id += 1

    blocks_to_order = list(blocks)
    compact_blocks = []
    free_spaces = []

    while blocks_to_order:
        block = blocks_to_order.pop(0)

        if block == '.':
            free_spaces.append(block)

            if not blocks_to_order:
                break
            right_block = blocks_to_order.pop(-1)

            while right_block == '.':
                free_spaces.append('.')

                if not blocks_to_order:
                    break
                right_block = blocks_to_order.pop(-1)
            else:
                compact_blocks.append(right_block)
        else:
            compact_blocks.append(block)

    result = 0
    for i, block in enumerate(compact_blocks):
        result += i * int(block)

    print(blocks)
    print(compact_blocks + free_spaces)
    print(result)


if __name__ == '__main__':
    main()
