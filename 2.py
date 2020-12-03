import sys
import re


def parse_line(l):
    pos, target, passwd = re.match(r"(\d+-\d+) (.): (.*)", l).groups()
    positions = [int(x) for x in pos.split("-")]
    return positions, target, passwd


def count_falls_in_range(string, char, count_range):
    return string.count(char) in count_range


def one_index_has_char(string, char, indices):
    return (string[indices[0] - 1] == char) != (string[indices[1] - 1] == char)


def main():
    parsed_lines = [parse_line(l) for l in sys.stdin]

    ans1 = sum(
        [
            count_falls_in_range(password, target, range(ns[0], ns[1] + 1))
            for ns, target, password in parsed_lines
        ]
    )
    ans2 = sum(
        [
            one_index_has_char(password, target, ns)
            for ns, target, password in parsed_lines
        ]
    )
    print(ans1, ans2)


main()
