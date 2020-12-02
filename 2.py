import sys


def parse_line(l):
    inputs = l.split(" ")
    positions = [int(x) for x in inputs[0].split('-')]
    target = inputs[1].strip(':')
    passwd = inputs[2]

    return positions, target, passwd


def count_falls_in_range(string, char, count_range):
    return string.count(char) in count_range


def one_index_has_char(string, char, indices):
    return (string[indices[0]-1] == char) != (string[indices[1]-1] == char)


def main():
    parsed_lines = [parse_line(l) for l in sys.stdin]

    ans1 = sum([
        count_falls_in_range(password, target, range(ns[0], ns[1]+1))
        for ns, target, password in parsed_lines
    ])
    ans2 = sum([
        one_index_has_char(password, target, ns)
        for ns, target, password in parsed_lines
    ])
    print(ans1, ans2)


main()
