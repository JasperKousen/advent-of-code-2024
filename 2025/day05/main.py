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

    fresh_ingredients = []
    for line in data:
        ingredient = int(line.strip())

        for left, right in fresh_ingredient_ranges:
            if left <= ingredient <= right:
                fresh_ingredients.append(ingredient)
                break

    print(len(fresh_ingredients))


if __name__ == '__main__':
    main()
