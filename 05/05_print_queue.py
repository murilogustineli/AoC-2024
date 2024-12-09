"""
https://adventofcode.com/2024/day/5
"""

from data_05 import page_ordering_rules, updates

# sample data
sample_ordering_rules = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
"""

sample_updates = """
75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def load_data(content: str) -> list[str]:
    data = content.split("\n")
    return data[1:-1]  # remove empty strings


def get_page_ordering_rules(data: list[str]) -> dict[str, str]:
    page_rules = {}
    for order in data:
        x, y = order.split("|")
        page_rules[x] = y
    return page_rules


if __name__ == "__main__":
    # page ordering rules and updates
    page_data = load_data(sample_ordering_rules)
    updates = load_data(sample_updates)
    page_rules = get_page_ordering_rules(page_data)
    print(page_rules)
    print(updates)

    # Part One
