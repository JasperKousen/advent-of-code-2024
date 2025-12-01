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
        blocks.append((int(file), id))
        if int(space):
            blocks.append((int(space), None))
        id += 1

    blocks_to_order = blocks.copy()
    compact_blocks = []

    while blocks_to_order:
        space, id = blocks_to_order.pop(0)

        if id is not None:
            compact_blocks.append((space, id))
        else:
            for i, (right_space, right_id) in enumerate(reversed(blocks_to_order), start=1):
                if right_id is None:
                    continue

                if right_space > space:
                    continue

                compact_blocks.append(blocks_to_order.pop(-i))
                if i == 1:
                    blocks_to_order.append((right_space, None))
                else:
                    blocks_to_order.insert(-i + 1, (right_space, None))

                if right_space < space:
                    blocks_to_order.insert(0, (space - right_space, None))

                break
            else:
                compact_blocks.append((space, id))


    compacted_blocks = []
    for space, id in compact_blocks:
        if id is None:
            id = '.'

        compacted_blocks.extend(space * [str(id)])

    result = 0
    for i, block in enumerate(compacted_blocks):
        if block == '.':
            continue
        result += i * int(block)

    print(blocks)
    print(compact_blocks)
    print(''.join(compacted_blocks))
    print(result)

if __name__ == '__main__':
    main()
