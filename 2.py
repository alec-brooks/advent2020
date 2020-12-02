import sys


def parseLine(l):
    inputs = l.split(" ")
    positions = [int(x) for x in inputs[0].split('-')]
    target = inputs[1].strip(':')
    passwd = inputs[2]

    return positions, target, passwd


def main():
    c = 0
    for line in sys.stdin:
        positions, char, pwd = parseLine(line)
        if (pwd[positions[0]-1] == char) != (pwd[positions[1]-1] == char):
            c += 1
    print(c)


main()
