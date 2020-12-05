import sys


def main():
    seat_ids = [get_seat_id(x.strip()) for x in sys.stdin]
    ss = sorted(seat_ids)
    start = 32
    for s in ss:
        if s != start:
            return print(s-1)
        start+=1

def bin_string_to_int(bin_string, zero_char):
    return int(''.join(["0" if x == zero_char else "1" for x in bin_string]),2)

def get_seat_id(bp):
    row = bin_string_to_int(bp[:7], 'F')
    column = bin_string_to_int(bp[7:], 'L')
    return row * 8 + column


main()
