#!/usr/bin/env python

from sys import argv
from ..util import *

def do(input_file):
    lines = read_to_ints(input_file)
    return len([True for i in range(1, len(lines)) if lines[i] > lines[i-1]])

def do2(input_file):
    lines = read_to_ints(input_file)
    return len([True for i in range(1, len(lines)-2) if sum(lines[i:i+2]) > sum(lines[i-1:i+1])])

if __name__ == "__main__":
    print(do(argv[1]))
    print(do2(argv[1]))
