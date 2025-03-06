#!/usr/bin/env python3
# https://adventofcode.com/2015/day/7


def solve(input):
    def value(index_or_digits):
        return (
            int(index_or_digits)
            if index_or_digits.isdigit()
            else circuit[index_or_digits]
        )

    input = input.split("\n")
    circuit = {}

    while input:
        line = input.pop(0)
        if not line:
            continue
        l = line.split(" ")
        count = len(l)
        try:
            if count == 3:
                # "->"
                op1 = value(l[0])
                target = l[2]
                circuit[target] = op1
            elif count == 4:
                # "NOT"
                source = l[1]
                target = l[3]
                circuit[target] = ~(circuit[source]) & 0xFFFF
            elif count == 5:
                op1 = value(l[0])
                op2 = value(l[2])
                operator = l[1]
                target = l[4]
                circuit[target] = operate(op1, op2, operator)
        except KeyError as e:
            input.append(line)

    print(circuit["a"])


def operate(op1, op2, operator):
    if operator == "AND":
        return op1 & op2
    if operator == "OR":
        return op1 | op2
    if operator == "RSHIFT":
        return (op1 >> op2) & 0xFFFF
    if operator == "LSHIFT":
        return (op1 << op2) & 0xFFFF


if __name__ == "__main__":
    with open("data/7") as f:
        input = f.read()
    solve(input)
