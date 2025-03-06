#!/usr/bin/env python3
# https://adventofcode.com/2015/day/8


def solve(input):
    code_chars = 0
    mem_chars = 0

    for line in input.split("\n"):
        if not line:
            break
        code_chars += len(line)
        backslashes = line.count("\\")
        quotes = line.count('"')
        mem_chars += (
            len(line) + backslashes + quotes + 2
        )  # for starting and endng quotes

    print(code_chars, mem_chars, mem_chars - code_chars)


if __name__ == "__main__":
    with open("data/8") as f:
        input = f.read()
    solve(input)
