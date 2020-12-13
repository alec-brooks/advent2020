import sys

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'

cardinal_directions = {
    NORTH: (1, 0),
    SOUTH: (-1, 0),
    EAST: (0, 1),
    WEST: (0, -1),
}
FORWARD = 'F'
RIGHT = 'R'
LEFT = 'L'


def turn_around(x, y):
    return (x*-1, y*-1)


def right_90(x, y):
    return (y*-1, x)


def left_90(x, y):
    return (y, x*-1)


r = {
    90: right_90,
    180: turn_around,
    270: left_90
}
l = {
    90: left_90,
    180: turn_around,
    270: right_90
}


def manhattan_distance(moves_made):
    return sum([abs(sum(x)) for x in zip(*moves_made)])


def ans1(navigation):
    direction = cardinal_directions[EAST]
    moves_made = []
    for command in navigation:
        operation, *number = command
        n = int(''.join(number))
        if operation in cardinal_directions:
            moves_made.append([n * x for x in cardinal_directions[operation]])

        if operation == FORWARD:
            moves_made.append([n * x for x in direction])

        if operation == RIGHT:
            direction = r[n](*direction)

        if operation == LEFT:
            direction = l[n](*direction)

    return manhattan_distance(moves_made)


def ans2(navigation):
    moves_made = []
    waypoint_relative = (1, 10)
    for command in navigation:
        operation, *number = command
        n = int(''.join(number))
        if operation in cardinal_directions:
            dx, dy = [n * x for x in cardinal_directions[operation]]
            waypoint_relative = (
                waypoint_relative[0] + dx, waypoint_relative[1] + dy
            )

        if operation == FORWARD:
            moves_made.append([n * x for x in waypoint_relative])

        if operation == RIGHT:
            waypoint_relative = r[n](*waypoint_relative)
        if operation == LEFT:
            waypoint_relative = l[n](*waypoint_relative)
    return manhattan_distance(moves_made)


def main():
    navigation = [x.strip() for x in sys.stdin]
    print(ans1(navigation))
    print(ans2(navigation))


main()
