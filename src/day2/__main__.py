#!/usr/bin/env python

from sys import argv
from ..util import *

def do(input_file):
    input = read_to_strings(input_file)
    depth, distance = 0, 0
    for line in input:
        direction, amount = line.strip().split(' ')
        match direction:
            case 'forward':
                distance += int(amount)
            case 'up':
                depth -= int(amount)
            case 'down':
                depth += int(amount)
    return depth * distance

def do2(input_file):
    input = read_to_strings(input_file)
    return input_file

if __name__ == "__main__":
    print(do(argv[1]))
    print(do2(argv[1]))
