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

sample_data_2 = """
XMAS
SAMX
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


def make_grid(data: list[str]) -> list[list[str]]:
    grid = []
    for line in data:
        row = []
        for letter in line:
            row.append(letter)
        grid.append(row)
    return grid


def get_length_height(grid: list[list[str]]) -> tuple[int, int]:
    length = len(grid[0])
    height = len(grid)
    return length, height


def search2D(grid, row, col, word: str = "XMAS"):
    length, height = get_length_height(grid)
    counter = 0

    if grid[row][col] != word[0]:
        return False

    # x and y are used to set the direction of search
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    # traverse grid in all 8 directions
    for dir in range(8):
        # initialize starting point for current direction
        k, rd, cd = 1, row + x[dir], col + y[dir]

        # first character is already checked, match remaining characters
        for k in range(1, len(word)):
            # if out of bound break
            if rd >= height or rd < 0 or cd >= length or cd < 0:
                break

            # if not matched, break
            if grid[rd][cd] != word[k]:
                break

            # move in current direction
            rd += x[dir]
            cd += y[dir]
            k += 1

        # if all character matched, k will be equal to len(word)
        if k == len(word):
            counter += 1
            # print(row, col)
    return counter


def search_grid(grid: list[list[str]], length: int, height: int) -> int:
    total = 0
    for i in range(height):
        for j in range(length):
            if grid[i][j] == "X":
                counter = search2D(grid, i, j, "XMAS")
                total += counter
    return total


if __name__ == "__main__":
    # Part One
    sample_data = load_sample_data(sample_data)
    data = load_data("data_04.txt")
    grid = make_grid(data)
    length, height = get_length_height(grid)
    total = search_grid(grid, length, height)
    print(f"total: {total}")
