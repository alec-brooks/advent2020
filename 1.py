import sys
from itertools import combinations
from math import prod


def main():
    report = [int(x) for x in sys.stdin]
    print(expense_summing(report, 2020, 2))
    print(expense_summing(report, 2020, 3))


def expense_summing(report, target, number_of_items):
    for combo in combinations(report, number_of_items):
        if sum(combo) == target:
            return prod(combo)


main()
