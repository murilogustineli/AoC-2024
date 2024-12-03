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


def check_safe_levels(data: list):
    # check if all levels are safe
    safe_levels = 0
    for report in data:
        # check if all levels are either all increasing or all decreasing
        # any two adjacent levels differ by at least one and at most three
        # check if all levels are increasing
        if all([1 <= report[i] - report[i - 1] <= 3 for i in range(1, len(report))]):
            safe_levels += 1
        # check if all levels are decreasing
        elif all([1 <= report[i - 1] - report[i] <= 3 for i in range(1, len(report))]):
            safe_levels += 1
    return safe_levels


if __name__ == "__main__":
    data = load_data(file_path="data_02.txt")
    parsed_data = parse_data(data)
    safe_levels = check_safe_levels(parsed_data)
    print(f"safe levels: {safe_levels}")
