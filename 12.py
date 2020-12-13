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


def parse_command(command):
    operation, *number = command
    n = int(''.join(number))
    return operation, n


def ship_navigation(navigation, direction=cardinal_directions[EAST], moves_made=[]):
    if navigation == []:
        return manhattan_distance(moves_made)
    command, *future_navigation = navigation
    operation, n = parse_command(command)

    if operation in cardinal_directions:
        new_moves = moves_made + \
            [[n * x for x in cardinal_directions[operation]]]
        return ship_navigation(future_navigation, direction, new_moves)

    if operation == FORWARD:
        new_moves = moves_made + [[n * x for x in direction]]
        return ship_navigation(future_navigation, direction, new_moves)

    if operation == RIGHT:
        return ship_navigation(future_navigation, r[n](*direction), moves_made)

    if operation == LEFT:
        return ship_navigation(future_navigation, l[n](*direction), moves_made)


def waypoint_navigation(navigation, waypoint_relative=(1, 10), moves_made=[]):
    if navigation == []:
        return manhattan_distance(moves_made)

    command, *future_navigation = navigation
    operation, n = parse_command(command)

    if operation in cardinal_directions:
        dx, dy = [n * x for x in cardinal_directions[operation]]
        new_waypoint_relative = (
            waypoint_relative[0] + dx, waypoint_relative[1] + dy
        )
        return waypoint_navigation(future_navigation, new_waypoint_relative, moves_made)

    if operation == FORWARD:
        new_moves = moves_made + [[n * x for x in waypoint_relative]]
        return waypoint_navigation(future_navigation, waypoint_relative, new_moves)

    if operation == RIGHT:
        return waypoint_navigation(future_navigation, r[n](*waypoint_relative), moves_made)
    if operation == LEFT:
        return waypoint_navigation(future_navigation, l[n](*waypoint_relative), moves_made)


def main():
    navigation = [x.strip() for x in sys.stdin]
    print(ship_navigation(navigation))
    print(waypoint_navigation(navigation))


main()
