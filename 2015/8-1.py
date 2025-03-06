#!/usr/bin/env python3
# https://adventofcode.com/2015/day/8


def solve(input):
    code_chars = 0
    mem_chars = 0

    for line in input.split("\n"):
        if not line:
            break
        code_chars += len(line)
        i = 1  # skip first character, a double-quote
        while i < len(line) - 1:  # skip last character, also a double-quote
            c = line[i]
            if c == "\\":
                c2 = line[i + 1]
                if c2 == "\\" or c2 == '"':
                    i += 2
                elif c2 == "x":
                    i += 4
            else:
                i += 1
            mem_chars += 1

    print(code_chars, mem_chars, code_chars - mem_chars)


if __name__ == "__main__":
    with open("data/8") as f:
        input = f.read()
    solve(input)
