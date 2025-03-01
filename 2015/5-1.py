#!/usr/bin/env python3
# https://adventofcode.com/2015/day/5

import re


def solve(input):
    nice = 0
    regexs = [
        r"[aeiouAEIOU].*[aeiouAEIOU].*[aeiouAEIOU]",
        r"([a-zA-Z])\1",
        r"^(?!.*(ab|cd|pq|xy)).*$",
    ]
    for line in input.split("\n"):
        if not line:
            break
        for regex in regexs:
            x = re.search(regex, line)
            if not x:
                break
        else:
            nice += 1
    print(nice)


if __name__ == "__main__":
    with open("data/5") as f:
        input = f.read()
    solve(input)
