#!/usr/bin/env python3
# https://adventofcode.com/2015/day/10


def solve(input):
    input = list(input)
    output = ""
    while input:
        c = input.pop(0)
        count = 1
        while input and input[0] == c:
            count += 1
            input.pop(0)
        output += f"{count}{c}"

    return output


if __name__ == "__main__":
    input = "1113222113"
    interations = (40, 50)
    # this is horribly inefficient and took a long time for 50.
    for i in range(1, 1 + max(interations)):
        input = solve(input)
        if i in interations:
            print(i, len(input))
