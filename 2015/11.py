#!/usr/bin/env python3
# https://adventofcode.com/2015/day/11
import re


def solve(input):
    def is_valid(password):
        if "i" in password or "o" in password or "l" in password:
            return False
        if not re.search(r"(.)\1.*(.)\2", password):
            return False
        if not re.search(
            r"abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz",
            password,
        ):
            return False
        return True

    def increment(password):
        if password[-1] == "z":
            return increment(password[:-1]) + "a"
        return password[:-1] + chr(ord(password[-1]) + 1)

    input = increment(input)
    while not is_valid(input):
        input = increment(input)
    return input


if __name__ == "__main__":
    input = "hepxcrrq"
    next_password = solve(input)
    print(next_password)
    print(solve(next_password))
