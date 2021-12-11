#!/usr/bin/env python

from sys import argv
from numpy import array
from statistics import mode
from ..util import *

def do(input_file):
    input = array(read_to_int_lists(input_file))
    most_common = int(''.join([str(mode(arr)) for arr in input.T]), 2)
    least_common = int(''.join([str((mode(arr) - 1) * -1) for arr in input.T]), 2)
    return most_common * least_common

def do2(input_file):
    input = read_to_int_lists(input_file)
    return input_file

if __name__ == "__main__":
    print(do(argv[1]))
    print(do2(argv[1]))
