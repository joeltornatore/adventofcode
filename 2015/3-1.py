#!/usr/bin/env python3
# https://adventofcode.com/2015/day/3


def solve(input):
    x = 0
    y = 0
    houses = set()
    for c in input:
        houses.add((x, y))
        if c == "^":
            y += 1
        elif c == "v":
            y -= 1
        elif c == ">":
            x += 1
        elif c == "<":
            x -= 1

    print(len(houses))


if __name__ == "__main__":
    with open("data/3") as f:
        input = f.read()
    solve(input)
