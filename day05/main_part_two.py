from collections import defaultdict


def order_pages(pages, orderings_before_to_after):
    ordered_pages = []
    for page in pages:
        pages_after = orderings_before_to_after.get(page, [])
        indexes = [ordered_pages.index(page_after) for page_after in pages_after if page_after in ordered_pages]

        if indexes:
            ordered_pages.insert(min(indexes), page)
        else:
            ordered_pages.append(page)

    return ordered_pages


def main():
    with open('input.txt') as f:
        data = f.read().split('\n\n')

#     data = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13
#
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47""".split('\n\n')

    ordering, updates = data[0].splitlines(), data[1].splitlines()
    ordering = [order.split('|') for order in ordering]

    possible_pages = set()
    orderings = defaultdict(set)
    orderings_before_to_after = defaultdict(set)
    for before, after in ordering:
        possible_pages.add(before)
        possible_pages.add(after)
        orderings[after].add(before)
        orderings_before_to_after[before].add(after)

    correct_middle_pages = []

    for update in updates:
        invalid_pages = set()

        pages = update.split(',')
        for page in pages:
            if page in invalid_pages:
                break

            invalid_pages.update(orderings[page])
        else:
            continue

        # Invalid page
        pages = order_pages(pages, orderings_before_to_after)
        middle_page = pages[len(pages) // 2]
        correct_middle_pages.append(middle_page)

    print(correct_middle_pages)
    print(sum(int(page) for page in correct_middle_pages))


if __name__ == '__main__':
    main()
