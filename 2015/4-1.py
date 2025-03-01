#!/usr/bin/env python3
# https://adventofcode.com/2015/day/4
# this includes both parts, finding the hex that starts with 5 and 6 zeros.

from hashlib import md5


def solve():
    number = 0
    key = "ckczppom"
    found5 = False
    while True:
        string = f"{number}{key}"
        if not found5 and md5(f"{key}{number}".encode()).hexdigest().startswith(
            "00000"
        ):
            print(number)
            found5 = True
        if md5(f"{key}{number}".encode()).hexdigest().startswith("000000"):
            print(number)
            return
        number += 1


if __name__ == "__main__":
    solve()
