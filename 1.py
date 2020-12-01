import sys


def main():
    nums = [int(x) for x in sys.stdin]
    for ni in nums:
        for nj in nums:
            for nk in nums:
                if ni + nj + nk == 2020:
                    print(ni * nj * nk)


main()
