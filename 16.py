import sys
from collections import Counter
from math import prod

rules = {
    "departure location": lambda x: x in range(31, 538 + 1) or x in range(546, 960 + 1),
    "departure station": lambda x: x in range(39, 660 + 1) or x in range(673, 960 + 1),
    "departure platform": lambda x: x in range(35, 731 + 1) or x in range(745, 968 + 1),
    "departure track": lambda x: x in range(43, 179 + 1) or x in range(185, 953 + 1),
    "departure date": lambda x: x in range(29, 250 + 1) or x in range(263, 949 + 1),
    "departure time": lambda x: x in range(43, 903 + 1) or x in range(928, 954 + 1),
    "arrival location": lambda x: x in range(46, 372 + 1) or x in range(384, 968 + 1),
    "arrival station": lambda x: x in range(36, 215 + 1) or x in range(225, 950 + 1),
    "arrival platform": lambda x: x in range(25, 631 + 1) or x in range(655, 950 + 1),
    "arrival track": lambda x: x in range(26, 768 + 1) or x in range(781, 962 + 1),
    "class": lambda x: x in range(29, 462 + 1) or x in range(478, 974 + 1),
    "duration": lambda x: x in range(34, 441 + 1) or x in range(455, 963 + 1),
    "price": lambda x: x in range(39, 683 + 1) or x in range(693, 956 + 1),
    "route": lambda x: x in range(36, 342 + 1) or x in range(348, 971 + 1),
    "row": lambda x: x in range(37, 501 + 1) or x in range(520, 963 + 1),
    "seat": lambda x: x in range(46, 356 + 1) or x in range(369, 973 + 1),
    "train": lambda x: x in range(43, 414 + 1) or x in range(423, 954 + 1),
    "type": lambda x: x in range(35, 160 + 1) or x in range(178, 950 + 1),
    "wagon": lambda x: x in range(29, 878 + 1) or x in range(889, 959 + 1),
    "zone": lambda x: x in range(31, 188 + 1) or x in range(201, 971 + 1),
}
your_ticket = [
    137,
    149,
    139,
    127,
    83,
    61,
    89,
    53,
    73,
    67,
    131,
    113,
    109,
    101,
    71,
    59,
    103,
    97,
    107,
    79,
]

nearby_tickets = [x.strip().split(",") for x in sys.stdin]


def ans1(nearby_tickets):
    valid_ticket_fields = [
        (field, any([rule(int(field)) for rule in rules.values()]))
        for ticket in nearby_tickets
        for field in ticket
    ]
    return sum([int(f) for f, v in valid_ticket_fields if not v])


def is_valid(ticket):
    return all([any([rule(int(field)) for rule in rules.values()]) for field in ticket])


def ans2(nearby_tickets, your_ticket):
    valid_tickets = [ticket for ticket in nearby_tickets if is_valid(ticket)]
    valid_indexes = {}
    for i, rule_name in enumerate(rules):
        valid_rule_indexes = [
            idx
            for ticket in valid_tickets
            for idx, field in enumerate(ticket)
            if rules[rule_name](int(field))
        ]

        valid_indexes[rule_name] = [
            idx
            for idx, count in Counter(valid_rule_indexes).most_common()
            if count == len(valid_tickets)
        ]
    field_to_positions = {}
    while len(field_to_positions) < len(nearby_tickets[0]) and len(valid_indexes) != 0:
        counts = {len(valid_idxs): rn for rn, valid_idxs in valid_indexes.items()}
        if 1 in counts:
            field = counts[1]
            index = valid_indexes[field][0]
            field_to_positions[field] = valid_indexes[field][0]
            del valid_indexes[field]
            for rn, idxs in valid_indexes.items():
                valid_indexes[rn] = [ix for ix in idxs if ix != index]

        for i in range(len(nearby_tickets[0])):
            if sum([valid_idxs.count(i) for valid_idxs in valid_indexes.values()]) == 1:
                field = [
                    rn
                    for rn, valid_idxs in valid_indexes.items()
                    if valid_idxs.count(i) == 1
                ][0]
                field_to_positions[field] = i
                del valid_indexes[field]
                for rn, idxs in valid_indexes.items():
                    valid_indexes[rn] = [ix for ix in idxs if ix != i]

    departure_idxs = [
        i for f, i in field_to_positions.items() if f.startswith("departure")
    ]
    return prod([your_ticket[di] for di in departure_idxs])


def main():

    print(ans1(nearby_tickets))
    print(ans2(nearby_tickets, your_ticket))


main()
