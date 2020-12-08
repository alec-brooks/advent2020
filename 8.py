import sys
import re


def parse_line(l):
    return l.split(" ")


def perform_instruction(instructions, index=0, visited_indices=[], acc=0):
    if index > len(instructions) - 1:
        return acc
    operation, value = instructions[index]
    value = int(value)

    if index in visited_indices:
        return None
    if operation == "nop":
        return perform_instruction(
            instructions, index + 1, visited_indices + [index], acc
        )
    if operation == "acc":
        return perform_instruction(
            instructions,
            index + 1,
            visited_indices + [index],
            acc + value,
        )
    if operation == "jmp":
        return perform_instruction(
            instructions,
            index + value,
            visited_indices + [index],
            acc,
        )


def main():
    instructions = [parse_line(x.strip()) for x in sys.stdin]
    for i, ops in enumerate(instructions):
        if ops[0] == "acc":
            pass
        if ops[0] == "nop":
            instr = instructions.copy()
            instr[i] = ["jmp", ops[1]]
            res = perform_instruction(instr)
            if res is not None:
                print("res", res)
        if ops[0] == "jmp":
            instr = instructions.copy()
            instr[i] = ["nop", ops[1]]
            res = perform_instruction(instr)
            if res is not None:
                print("res", res)


main()
