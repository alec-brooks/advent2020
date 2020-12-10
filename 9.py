import sys
from itertools import combinations, chain


def silver(ns):
    for i in range(25, len(ns)):
        adders = combinations(ns[i-25:i], 2)
        if not any([(a[0] + a[1]) == ns[i] for a in adders]):
            return ns[i]

def gold(ns, ans):
    for w in range(2, len(ns)+1):
        for i in range(len(ns)-w+1):
            sublist = ns[i:i+w]
            if sum(sublist) == ans:
                return min(sublist) + max(sublist)



def main():
    ns = [int(x.strip()) for x in sys.stdin]
    ans1 = silver(ns)
    print(ans1)
    print(gold(ns, ans1))


main()
