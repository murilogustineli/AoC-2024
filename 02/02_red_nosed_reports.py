sample_data = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]


def load_data(file_path: str):
    with open(file_path, "r") as file:
        content = file.read()
        data = content.split("\n")
    return data


def parse_data(data: list):
    # parse data into a list of integers
    final_data = []
    for report in data:
        report = report.split(" ")
        report = [int(level) for level in report]
        final_data.append(report)
    return final_data


def is_safe(levels):
    if len(levels) <= 1:
        return True

    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    # Check for zero differences
    if any(diff == 0 for diff in diffs):
        return False

    # Check differences are between 1 and 3 inclusive (absolute value)
    if not all(1 <= abs(diff) <= 3 for diff in diffs):
        return False

    # Check all differences are in the same direction
    if all(diff > 0 for diff in diffs):
        return True
    if all(diff < 0 for diff in diffs):
        return True

    return False


def is_safe_with_removal(levels):
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1 :]
        if is_safe(new_levels):
            return True
    return False


def main():
    # Part One
    data = load_data(file_path="data_02.txt")
    reports = parse_data(data)
    # Part One
    safe_reports_part1 = sum(1 for report in reports if is_safe(report))
    print(f"\nPart One: Number of safe reports is {safe_reports_part1}")

    # Part Two
    safe_reports_part2 = sum(1 for report in reports if is_safe_with_removal(report))
    print(f"Part Two: Number of safe reports is {safe_reports_part2}")


if __name__ == "__main__":
    main()
