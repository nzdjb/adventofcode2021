#!/usr/bin/env python

from sys import argv
from numpy import array, where
from ..util import *

dcoords = [(x, y) for y in range(-1,2) for x in range(-1,2) if (x, y) != (0, 0)]

def do(input_file):
    input = array(read_to_int_lists(input_file))
    total = 0
    for _ in range(100):
        input = input + 1
        input = find_flashes(input, [])
        flashes = list(zip(*where(input >= 10)))
        total += len(flashes)
        for x, y in flashes:
            input[x][y] = 0

    return total

def find_flashes(input, flashes = []):
    new_flashes = [flash for flash in list(zip(*where(input >= 10))) if flash not in flashes]
    for x, y in [(x + dx, y + dy) for dx, dy in dcoords for x, y in new_flashes]:
        if x in range(0, 10) and y in range(0, 10) and input[x][y] < 10 and (x, y) not in flashes:
            input[x][y] += 1
    flashes += new_flashes
    if new_flashes:
        input = find_flashes(input, flashes)
    return input

def do2(input_file):
    return input_file

if __name__ == "__main__":
    print(do(argv[1]))
    print(do2(argv[1]))
