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


def check_safe_levels(data: list, problem_dampener: bool = False):
    # check if all levels are safe
    safe_levels = 0
    for report in data:
        # check if all levels are either all increasing or all decreasing
        # any two adjacent levels differ by at least one and at most three
        # check if all levels are increasing
        increasing = [
            1 <= report[i] - report[i - 1] <= 3 for i in range(1, len(report))
        ]
        # check if all levels are decreasing
        decreasing = [
            1 <= report[i - 1] - report[i] <= 3 for i in range(1, len(report))
        ]
        if problem_dampener:
            if (
                sum(increasing) == len(increasing) - 1
                or sum(decreasing) == len(decreasing) - 1
            ):
                safe_levels += 1
                print(f"safe: {report}")
                continue
        if all(increasing) or all(decreasing):
            safe_levels += 1
            print(f"safe: {report}")
        else:
            print(f"unsafe: {report}")
    return safe_levels


if __name__ == "__main__":
    # Part One
    data = load_data(file_path="data_02.txt")
    parsed_data = parse_data(data[:10])
    # safe_levels = check_safe_levels(parsed_data)
    # print(f"safe levels: {safe_levels}")
    # Par Two
    safe_levels = check_safe_levels(parsed_data, problem_dampener=True)
    print(f"safe levels problem dampener: {safe_levels}")
