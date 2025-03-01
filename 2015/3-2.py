#!/usr/bin/env python3
# https://adventofcode.com/2015/day/3


class santa:
    def __init__(self):
        self.x = 0
        self.y = 0


def solve(input):
    bots = [santa(), santa()]
    houses = set()
    houses.add((0, 0))
    toggle = True
    for c in input.strip():
        bot = bots[toggle]
        if c == "^":
            bot.y += 1
        elif c == "v":
            bot.y -= 1
        elif c == ">":
            bot.x += 1
        elif c == "<":
            bot.x -= 1

        houses.add((bot.x, bot.y))
        toggle = not toggle

    print(len(houses))


if __name__ == "__main__":
    with open("data/3") as f:
        input = f.read()
    solve(input)
