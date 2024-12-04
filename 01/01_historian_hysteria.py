"""
https://adventofcode.com/2024/day/1
"""

from collections import Counter


# read txt data file
def load_data(file_path: str):
    with open(file_path, "r") as file:
        content = file.read()
        data_pair = content.split("\n")
    # split data pair into left and right lists
    left_list, right_list = [], []
    for pair in data_pair:
        pair = pair.split("   ")
        left_list.append(int(pair[0]))
        right_list.append(int(pair[1]))
    return left_list, right_list


def find_total_distance(left_list: list, right_list: list):
    # order data
    left_list.sort()
    right_list.sort()
    # find total distance between the left and right lists
    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(int(left_list[i]) - int(right_list[i]))
    return total_distance


def similarity_score(left_list: list, right_list: list):
    # count the number of similar elements
    counter = Counter(right_list)
    total_similarity = 0
    for num in left_list:
        if num in counter:
            total_similarity += num * counter[num]
    return total_similarity


if __name__ == "__main__":
    left_list, right_list = load_data("data_01.txt")
    # find total distance between the left and right lists
    total_distance = find_total_distance(left_list, right_list)
    print(f"total distance: {total_distance}")
    # count the number of similar elements
    counter = similarity_score(left_list, right_list)
    print(f"total similarity: {counter}")
