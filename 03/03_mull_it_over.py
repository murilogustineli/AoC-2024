sample_instructions = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)


def load_data(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()
    return content


def find_multiplications(instructions: str) -> list:
    # search for mul() in the instructions
    multiplications = re.findall(r"mul\((\d+),(\d+)\)", instructions)
    return multiplications


def multiply_and_sum(multiplications: list) -> int:
    # multiply the two numbers in each tuple
    result = [int(x) * int(y) for x, y in multiplications]
    # sum the results
    result = sum(result)
    return result


def extract_patterns(instructions: str) -> list:
    # search for mul(), do() and dont() in the sample_instructions
    mul_pattern = r"mul\(\d+,\d+\)|do\(\)|don'?t\(\)"
    pattern = re.finditer(mul_pattern, instructions)
    return [p.group() for p in pattern]


def process_matches(patterns: list) -> list:
    # process the matches
    mul_enabled = True
    processed_patterns = []
    for pattern in patterns:
        if pattern == "don't()":
            mul_enabled = False
        elif pattern == "do()":
            mul_enabled = True
        elif mul_enabled:
            processed_patterns.append(pattern)
    return processed_patterns


def find_multiplications_part_two(patterns: list) -> list:
    # search for mul() in the instructions
    string = ""
    for i in patterns:
        string += str(i)
    multiplications = re.findall(r"mul\((\d+),(\d+)\)", string)
    return multiplications


if __name__ == "__main__":
    import re

    # load data
    instructions = load_data("data_03.txt")

    # Part One
    multiplications = find_multiplications(instructions)
    result = multiply_and_sum(multiplications)
    print(f"Part One: {result}")

    # Part Two
    patterns = extract_patterns(instructions)
    processed_patterns = process_matches(patterns)
    multiplications = find_multiplications_part_two(processed_patterns)
    result = multiply_and_sum(multiplications)
    print(f"Part Two: {result}")
