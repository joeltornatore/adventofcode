#!/usr/bin/env python3
# https://adventofcode.com/2015/day/1

import sys


def solve(input):
    step = 0
    floor = 0
    for c in input:
        step += 1
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
            if floor < 0:
                print(step)
                sys.exit()


if __name__ == "__main__":
    with open("data/1") as f:
        input = f.read()
    solve(input)
