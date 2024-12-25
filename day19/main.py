import re

from tqdm import tqdm
import functools



# def find_combinations(design, patterns):
#     combinations = set()
#     sorted_patterns = list(sorted(patterns, key=len, reverse=True))
#
#     regex_pattern = re.compile('^(?:' + '|'.join(pattern for pattern in sorted_patterns) + ')+$')
#     if regex_pattern.fullmatch(design):
#
#         find_pattern = re.compile('|'.join(sorted_patterns))
#
#         parts = []
#         index = 0
#         while index < len(design):
#             # Attempt to match at the current position
#             match = find_pattern.match(design, index)
#             if match:
#                 substr = match.group()
#                 parts.append(substr)
#                 index += len(substr)
#
#         # for i in range(1, len(design) + 1):
#         #     find_pattern = re.compile('^' + ('(?:(' + '|'.join(pattern for pattern in patterns) + '))') * i + '$')
#         #     parts = find_pattern.findall(design)
#         #
#         #     if parts:
#         #         break
#         # else:
#         #     return combinations
#         # find_pattern = re.compile('|'.join(pattern for pattern in patterns))
#         # parts = tuple(find_pattern.findall(design))
#         combinations.add(parts[0])
#
#         for part in parts[0]:
#             combinations.update(find_combinations(design, patterns - set([part])))
#
#     return combinations


def main():
    with open('input.txt') as f:
        data = f.read()

#     data = """r, wr, b, g, bwu, rb, gb, br
#
# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb"""

    data = data.splitlines()

    patterns = data.pop(0).split(', ')
    patterns = patterns
    sorted_patterns = sorted(patterns, key=len, reverse=True)

    data.pop(0)
    designs = data

    @functools.cache
    def find_combinations(design):
        if not design:
            return 1

        count = 0
        for pattern in sorted_patterns:
            if design.startswith(pattern):
                count += find_combinations(design[len(pattern):])

        return count

    regex_pattern = re.compile('^(?:' + '|'.join(pattern for pattern in patterns) + ')+$')

    # for design in designs:
        # print(design, bool(regex_pattern.fullmatch(design)))
        # print(design, len(find_combinations(design, patterns)))

    print(sum(bool(regex_pattern.fullmatch(design)) for design in designs))
    print(sum(find_combinations(design) for design in tqdm(designs)))

    # print(patterns)
    # print(designs)


if __name__ == '__main__':
    main()
