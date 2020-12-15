import sys
import re
import itertools

MASK = "mask"
MEM = "mem"


def parse_mask(l):
    _, n = l.split(" = ")
    return (MASK, n)


def parse_mem(l):
    address, value = re.match(r"mem\[(\d+)\] = (\d+)", l).groups()
    return (MEM, (int(address), int(value)))


def parse_line(l):
    return parse_mask(l) if l.startswith("mask") else parse_mem(l)


def bitmask(b, mask):
    return int("".join([x if m == "X" else m for x, m in zip(b, mask)]), 2)


def float_bitmask(bin_str, mask):
    def apply_mask(b, m):
        if m == "0":
            return str(b)
        if m == "1":
            return "1"
        if m == "X":
            return "X"

    float_mask = [apply_mask(b, m) for b, m in zip(bin_str, mask)]
    x_positions = [pos for pos, char in enumerate(float_mask) if char == "X"]
    x_combos = itertools.product(["0", "1"], repeat=len(x_positions))
    r = []
    for x_combo in x_combos:
        s = list(float_mask)
        for p, b in zip(x_positions, x_combo):
            s[p] = b
        r.append(int("".join(s), 2))
    return r


def ans1(lines):
    memory = {}
    for operation, value in lines:
        if operation == MASK:
            active_mask = value
        if operation == MEM:
            binary_string = "{0:b}".format(value[1]).zfill(36)
            memory[value[0]] = bitmask(binary_string, active_mask)
    return sum(memory.values())


def ans2(lines):
    memory = {}
    for operation, value in lines:
        if operation == MASK:
            active_mask = value
        if operation == MEM:
            binary_string = "{0:b}".format(value[0]).zfill(36)
            mem_addresses = float_bitmask(binary_string, active_mask)
            for mem_addr in mem_addresses:
                memory[mem_addr] = value[1]
    return sum(memory.values())


def main():
    data = sys.stdin
    lines = [parse_line(x) for x in data]
    print(ans1(lines))
    print(ans2(lines))


main()
