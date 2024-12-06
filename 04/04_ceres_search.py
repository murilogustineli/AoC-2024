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

sample_data_3 = """
M.S
.A.
M.S
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


def search2D(grid, row: int, col: int, word: str) -> int:
    length, height = get_length_height(grid)
    counter = 0

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


def search_grid(
    grid: list[list[str]],
    word: str = "XMAS",
) -> int:
    length, height = get_length_height(grid)
    total = 0
    for i in range(height):
        for j in range(length):
            if grid[i][j] == word[0]:
                counter = search2D(grid, i, j, word)
                total += counter
    return total


def search2D_XMAS(grid, row: int, col: int, word: str) -> int:
    length, height = get_length_height(grid)
    counter = 0

    # x and y are used to set the direction of search
    x = [1, -1, -1, 1]
    y = [1, 1, -1, -1]

    # traverse grid in all 4 directions in the X
    for dir in range(4):
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
            # check for MAS in the other direction of the X
            # dir=0,(3,3): (3,0), (0,3)
            # dir=2,(0,0): (3,0), (0,3)
            # dir=3,(3,0): (0,0), (3,3)
            # dir=1,(0,3): (0,0), (3,3)
            if dir == 0:
                if (
                    grid[rd - 1][cd - 3] == word[0]
                    and grid[rd - 2][cd - 2] == word[1]
                    and grid[rd - 3][cd - 1] == word[2]
                ):
                    counter += 1
                elif (
                    grid[rd - 3][cd - 1] == word[0]
                    and grid[rd - 2][cd - 2] == word[1]
                    and grid[rd - 1][cd - 3] == word[2]
                ):
                    counter += 1
            elif dir == 2:
                if (
                    grid[rd + 1][cd - 3] == word[0]
                    and grid[rd + 2][cd - 2] == word[1]
                    and grid[rd + 3][cd - 1] == word[2]
                ):
                    counter += 1
                elif (
                    grid[rd + 3][cd - 1] == word[0]
                    and grid[rd + 2][cd - 2] == word[1]
                    and grid[rd + 1][cd - 3] == word[2]
                ):
                    counter += 1
            elif dir == 3:
                if (
                    grid[rd - 3][cd + 1] == word[0]
                    and grid[rd - 2][cd + 2] == word[1]
                    and grid[rd - 1][cd + 3] == word[2]
                ):
                    counter += 1
                elif (
                    grid[rd - 1][cd + 3] == word[0]
                    and grid[rd - 2][cd + 2] == word[1]
                    and grid[rd - 3][cd + 1] == word[2]
                ):
                    counter += 1
            elif dir == 1:
                if (
                    grid[rd + 1][cd - 3] == word[0]
                    and grid[rd + 2][cd - 2] == word[1]
                    and grid[rd + 3][cd - 1] == word[2]
                ):
                    counter += 1
                elif (
                    grid[rd + 3][cd - 3] == word[0]
                    and grid[rd + 2][cd - 2] == word[1]
                    and grid[rd + 1][cd - 1] == word[2]
                ):
                    counter += 1
    return counter / 2


def search_grid_XMAS(
    grid: list[list[str]],
    word: str = "MAS",
) -> int:
    length, height = get_length_height(grid)
    total = 0
    for i in range(height):
        for j in range(length):
            if grid[i][j] == word[0]:
                counter = search2D_XMAS(grid, i, j, word)
                total += counter
    return total


if __name__ == "__main__":
    # Part One
    sample_data = load_sample_data(sample_data)
    data = load_data("data_04.txt")
    grid = make_grid(data)
    total = search_grid(grid)
    print(f"total: {total}")

    # Part Two
    sample_data = load_sample_data(sample_data_3)
    grid = make_grid(data)
    total = search_grid_XMAS(grid, word="MAS")
    print(f"total: {total}")
