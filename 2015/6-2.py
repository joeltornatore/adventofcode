#!/usr/bin/env python3
# https://adventofcode.com/2015/day/6


def solve(input):
    lights = [[0] * 1000 for _ in range(1000)]

    for line in input.split("\n"):
        if not line:
            break
        line = line.split(" ")
        if line[0] == "turn":
            (x1, y1) = line[2].split(",")
            (x2, y2) = line[4].split(",")
            (x1, y1, x2, y2) = (int(x1), int(y1), int(x2) + 1, int(y2) + 1)
            increment = 1 if line[1] == "on" else -1
            for x in range(x1, x2):
                for y in range(y1, y2):
                    lights[x][y] += increment
                    lights[x][y] = max(lights[x][y], 0)
        elif line[0] == "toggle":
            (x1, y1) = line[1].split(",")
            (x2, y2) = line[3].split(",")
            (x1, y1, x2, y2) = (int(x1), int(y1), int(x2) + 1, int(y2) + 1)
            for x in range(x1, x2):
                for y in range(y1, y2):
                    lights[x][y] += 2
        else:
            print("bad input")

    print(sum(sum(row) for row in lights))


if __name__ == "__main__":
    with open("data/6") as f:
        input = f.read()
    solve(input)
