def main():
    with open('input.txt') as f:
        data = f.readlines()

    diagram = [list(row.strip()) for row in data]

    splits = 0

    for row_nr in range(len(diagram) - 1):
        for col_nr in range(len(diagram[row_nr])):
            match diagram[row_nr][col_nr]:
                case 'S':
                    diagram[row_nr + 1][col_nr] = '|'
                case '|':
                    match diagram[row_nr + 1][col_nr]:
                        case '.':
                            diagram[row_nr + 1][col_nr] = '|'
                        case '^':
                            diagram[row_nr + 1][col_nr - 1] = '|'
                            diagram[row_nr + 1][col_nr + 1] = '|'

                            splits += 1
                case '.':
                    pass
                case '^':
                    pass

    print('\n'.join(''.join(row) for row in diagram))
    print(splits)

if __name__ == '__main__':
    main()
