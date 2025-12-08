from collections import Counter
from copy import deepcopy
from tqdm import tqdm

def main():
    with open('input.txt') as f:
        data = f.readlines()

    diagram = [list(row.strip()) for row in data]

    n_rows = len(diagram)
    n_cols = len(diagram[0])

    timelines = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    for row_nr in range(len(diagram) - 1):
        for col_nr in range(len(diagram[row_nr])):
            match diagram[row_nr][col_nr]:
                case 'S':
                    diagram[row_nr + 1][col_nr] = '|'
                    timelines[row_nr + 1][col_nr] += 1

                    timelines[row_nr][col_nr] = 'S'
                case '|':
                    match diagram[row_nr + 1][col_nr]:
                        case '.' | '|':
                            diagram[row_nr + 1][col_nr] = '|'
                            timelines[row_nr + 1][col_nr] += timelines[row_nr][col_nr]
                        case '^':
                            diagram[row_nr + 1][col_nr - 1] = '|'
                            diagram[row_nr + 1][col_nr + 1] = '|'
                            timelines[row_nr + 1][col_nr - 1] += timelines[row_nr][col_nr]
                            timelines[row_nr + 1][col_nr + 1] += timelines[row_nr][col_nr]
                case '.':
                    timelines[row_nr][col_nr] = '.'
                case '^':
                    timelines[row_nr][col_nr] = '^'

    # print('\n'.join(''.join(row) for row in diagram))
    print('\n'.join(''.join(str(t) for t in row) for row in timelines))
    print(sum(timelines[-1]))
if __name__ == '__main__':
    main()
