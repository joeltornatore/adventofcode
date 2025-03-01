#!/usr/bin/env python3
# https://adventofcode.com/2015/day/1

import sys


def solve(input):
    open_parens = input.count("(")
    close_parens = input.count(")")
    print(open_parens - close_parens)


if __name__ == "__main__":
    with open("data/1") as f:
        input = f.read()
    solve(input)
