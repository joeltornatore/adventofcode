#!/usr/bin/env python3
# https://adventofcode.com/2015/day/2


def solve(input):
    total = 0

    for line in input.split("\n"):
        if not line:
            break
        line = line.split("x")
        l = int(line[0])
        w = int(line[1])
        h = int(line[2])
        total += 2 * (l + w + h - max(l, w, h)) + l * w * h

    print(total)


if __name__ == "__main__":
    with open("data/2") as f:
        input = f.read()
    solve(input)
