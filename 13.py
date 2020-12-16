from sympy.ntheory.modular import crt
from functools import reduce
import sys
import math


def ans1(time, bus_shedule, wait=0):
    active_bus_schedule = [int(b) for b in bus_shedule if b != 'x']
    for bs in active_bus_schedule:
        if time % bs == 0:
            return bs * wait
    return ans1(time+1, bus_shedule, wait+1)


def schedule_aligned(t, bus_schedule):
    return all((t + relative_t) % bus == 0 for relative_t, bus in bus_schedule)


def main():
    timestamp, raw_bus_shedule = [x.strip() for x in sys.stdin]
    # timestamp, raw_bus_shedule = [x.strip() for x in test_data]

    bus_schedule = raw_bus_shedule.split(',')

    print(ans1(int(timestamp), bus_schedule))

    a, n = zip(*[(-i, int(bus))
                 for i, bus in enumerate(bus_schedule) if bus != 'x'])

    print(crt(n, a)[0])


main()
