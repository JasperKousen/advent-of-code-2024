from collections import deque

def main():
    with open('input.txt') as f:
        data = f.readlines()
    data = deque(data)

    fresh_ingredient_ranges = []
    while data:
        line = data.popleft().strip()
        if not line:
            break

        ingredient_range = line.split('-')

        fresh_ingredient_ranges.append(
            (
                int(ingredient_range[0]), int(ingredient_range[1]),
            )
        )

    fresh_ingredient_ranges.sort()

    new_ranges = []

    prev_right = 0
    for left, right in fresh_ingredient_ranges:
        if left <= prev_right:
            left = max(left, prev_right) + 1

        if left > right:
            continue

        new_ranges.append((left, right))
        prev_right = right

    fresh_ingredients = 0
    for left, right in new_ranges:
        fresh_ingredients += right - left + 1

    print(fresh_ingredient_ranges)
    print(new_ranges)
    print(fresh_ingredients)


if __name__ == '__main__':
    main()
