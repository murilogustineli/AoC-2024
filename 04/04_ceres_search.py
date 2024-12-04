"""
https://adventofcode.com/2024/day/4
https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/
"""

sample_data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def load_sample_data(string: str) -> list[str]:
    data = string.split("\n")
    data = [letters for letters in data if letters != ""]
    return data


def load_data(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        content = file.read()
        data = content.split("\n")
    return data


def get_length_height(data: list) -> tuple:
    length = len(data[0])
    height = len(data)
    return length, height


def make_grid(data: list[str]) -> list[list[str]]:
    grid = []
    for line in data:
        row = []
        for letter in line:
            row.append(letter)
        grid.append(row)
    return grid


def search2D(grid, row, col, word: str = "XMAS"):
    pass


if __name__ == "__main__":
    sample_data = load_sample_data(sample_data)
    data = load_data("data_04.txt")
    length, height = get_length_height(data=sample_data)
    grid = make_grid(sample_data)
    print(sample_data)
    print(f"grid: {length}, {height}")
