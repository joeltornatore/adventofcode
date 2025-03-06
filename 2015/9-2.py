#!/usr/bin/env python3
# https://adventofcode.com/2015/day/9

from itertools import permutations


def solve(input):
    cities = set()
    distances = {}

    for line in input.split("\n"):
        if not line:
            break
        line = line.split()
        city1 = line[0]
        city2 = line[2]
        distance = int(line[4])
        cities.add(city1)
        cities.add(city2)
        distances[(city1, city2)] = distance
        distances[(city2, city1)] = distance

    longest_distance = 0
    routes = permutations(cities)
    for route in routes:
        distance = 0
        route = list(route)
        location = route.pop(0)
        for next_city in route:
            distance += distances[(location, next_city)]
            location = next_city

        longest_distance = max(longest_distance, distance)

    print(longest_distance)


if __name__ == "__main__":
    with open("data/9") as f:
        input = f.read()
    solve(input)
