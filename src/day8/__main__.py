#!/usr/bin/env python

from sys import argv
from ..util import *

def do(input_file):
    lines = read_to_strings(input_file)
    total = 0
    for line in lines:
        _, output = parse_line(line)
        total += sum([len(digit) in [2, 3, 4, 7] for digit in output])
    return total

def do2(input_file):
    lines = read_to_strings(input_file)
    return input_file

def parse_line(line):
    (input, output) = [io.split(' ') for io in line.strip().split(' | ')]
    return (input, output)

if __name__ == "__main__":
    print(do(argv[1]))
    print(do2(argv[1]))
