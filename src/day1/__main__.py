#!/usr/bin/env python

from sys import argv
from ..util import *

def do(input_file):
    lines = read_to_ints(input_file)
    return len([True for i in range(len(lines)) if lines[i] != 0 and int(lines[i]) > int(lines[i-1])])

def do2(input_file):
    return input_file

if __name__ == "__main__":
    print(do(argv[1]))
    print(do2(argv[1]))
