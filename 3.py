import sys
from math import prod


def trees_hit_on_slope(course, slope):
    right, down = slope
    current_horizontal = 0
    count = 0
    for line_i in range(0, len(course), down):
        count += 1 if course[line_i][current_horizontal] == "#" else 0
        current_horizontal = (current_horizontal + right) % len(course[line_i])
    return count


def main():
    course = [x.strip() for x in sys.stdin]

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    print(prod([trees_hit_on_slope(course, slope) for slope in slopes]))


main()
