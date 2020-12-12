import sys
from itertools import combinations
from collections import defaultdict

test_data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split()

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

directions_to_check = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def is_inbound_and_target(x, y, seats, target):
    return x >= 0 and x < len(seats) \
        and y >= 0 and y < len(seats[0]) \
        and seats[x][y] == target


def count_adjacent(x, y, seats, target_count):
    return sum([1 for dx, dy in directions_to_check if is_inbound_and_target(x+dx, y+dy, seats, target_count)])


def line_of_sight(x, y, seats, target_count, dx, dy):
    new_x = x+dx
    new_y = y+dy
    if not ((0 <= new_x <= len(seats)-1) and (0 <= new_y <= len(seats[0])-1)):
        return False
    if seats[new_x][new_y] != '.':
        return seats[new_x][new_y] is target_count
    return line_of_sight(new_x, new_y, seats, target_count, dx, dy)


def count_seen_seats(x, y, seats, target_count):
    return sum([1 for x2, y2 in directions_to_check if line_of_sight(x, y, seats, target_count, x2, y2)])


def sum_occupied(seats):
    return sum([s == OCCUPIED for sr in seats for s in sr])


def silver_seat_assigner(seat, x, y, prev_seats):
    if seat is EMPTY and count_adjacent(x, y, prev_seats, OCCUPIED) == 0:
        return OCCUPIED
    if seat is OCCUPIED and count_adjacent(x, y, prev_seats, OCCUPIED) >= 4:
        return EMPTY
    return seat


def gold_seat_assigner(seat, x, y, prev_seats):
    if seat is EMPTY and count_seen_seats(x, y, prev_seats, OCCUPIED) == 0:
        return OCCUPIED
    if seat is OCCUPIED and count_seen_seats(x, y, prev_seats, OCCUPIED) >= 5:
        return EMPTY
    return seat


def new_seat_configuration(prev_seats, seat_assigner):
    new_seats = [
        [None for _ in range(len(prev_seats[0]))]
        for _ in range(len(prev_seats))
    ]
    for i, seat_row in enumerate(prev_seats):
        for j, seat in enumerate(seat_row):
            new_seats[i][j] = seat_assigner(seat, i, j, prev_seats)
    if prev_seats == new_seats:
        return sum_occupied(new_seats)
    return new_seat_configuration(new_seats, seat_assigner)


def main():
    seats = [x.strip() for x in sys.stdin]
    print(new_seat_configuration(seats, silver_seat_assigner))
    print(new_seat_configuration(seats, gold_seat_assigner))


main()
