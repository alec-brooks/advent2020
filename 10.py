import sys
from itertools import combinations_with_replacement
from collections import defaultdict


def main():
    a = """16
10
15
5
1
11
7
19
6
12
4""".split()
    jas = sorted([int(x.strip()) for x in a])
    # jas = sorted([int(x.strip()) for x in sys.stdin])
    device_ja = max(jas) + 3

    print(take_jolts(jas + [device_ja]))
    print(p2(jas))


def count_paths(jas, count=0):
    if jas == []:
        return count

    head_adapter, *new_jas = jas
    print(head_adapter)
    return count_paths(
        new_jas,
        count + sum([1 for x in [1, 2, 3] if head_adapter + x in new_jas])
    )


def p2(jas):
    dp = defaultdict(int)
    dp[0] = 1
    for n in jas:
        dp[n] += dp[n-1] + dp[n-2] + dp[n-3]
    return dp[max(dp)]


def take_jolts(jas, prev=0, ones_count=0, threes_count=0):
    if jas == []:
        return ones_count * threes_count

    head_adapter, *new_jas = jas

    return take_jolts(
        new_jas,
        head_adapter,
        ones_count + 1 if head_adapter - prev == 1 else ones_count,
        threes_count + 1 if head_adapter - prev == 3 else threes_count
    )


main()
