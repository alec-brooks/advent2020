import sys
sys.setrecursionlimit(30000000)


def target_word(target, last_number, last_occurred_dict, i):
    if i == target:
        return last_number
    new_number = 0

    if last_number in last_occurred_dict:
        new_number = i - last_occurred_dict[last_number]

    last_occurred_dict[last_number] = i

    return target_word(target, new_number, last_occurred_dict, i+1)


def main():
    target = 30000000
    ns = [20, 9, 11, 0, 1, 2]

    last_occurred_dict = {n: i+1 for i, n in enumerate(ns)}

    last_number = ns[-1]
    i = len(ns)
    while i != target:
        new_number = 0

        if last_number in last_occurred_dict:
            new_number = i - last_occurred_dict[last_number]

        last_occurred_dict[last_number] = i

        last_number = new_number
        i += 1

    print(i, last_number)


main()
