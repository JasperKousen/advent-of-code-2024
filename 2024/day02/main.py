import csv


def is_strictly_increasing(report):
    return all(y > x for x, y in zip(report, report[1:]))


def is_strictly_decreasing(report):
    return all(y < x for x, y in zip(report, report[1:]))


def has_only_small_steps(report):
    return all(1 <= abs(x - y) <= 3 for x, y in zip(report, report[1:]))


def is_safe(report, problem_dampener=True):
    report = [int(record) for record in report]

    if not problem_dampener:
        return (
            (is_strictly_increasing(report) or is_strictly_decreasing(report))
            and has_only_small_steps(report)
        )

    dampened_reports = [report[:i] + report[i + 1:] for i in range(len(report))]

    return any(
        (is_strictly_increasing(report) or is_strictly_decreasing(report))
        and has_only_small_steps(report)
        for report in dampened_reports
    )


def main():
    with open('input.txt') as f:
        reports = csv.reader(f, delimiter=' ')

        answer = sum(is_safe(report, problem_dampener=False) for report in reports)

        print(f'Answer Part One: {answer}')

    with open('input.txt') as f:
        reports = csv.reader(f, delimiter=' ')

        answer = sum(is_safe(report, problem_dampener=True) for report in reports)

        print(f'Answer Part Two: {answer}')


if __name__ == '__main__':
    main()
