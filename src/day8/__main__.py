#!/usr/bin/env python

from sys import argv
from ..util import *

easy_lengths = [2, 3, 4, 7]

def do(input_file):
    lines = read_to_strings(input_file)
    total = 0
    for line in lines:
        _, output = parse_line(line)
        total += sum([len(digit) in easy_lengths for digit in output])
    return total

def do2(input_file):
    lines = read_to_strings(input_file)
    total = 0
    for line in lines:
        mapping = {}
        input, output = parse_line(line)
        for digit in filter(lambda x: len(x) in easy_lengths, input):
            mapping[digit] = find_value(digit, mapping)
        for digit in filter(lambda x: len(x) == 6, input):
            mapping[digit] = find_value(digit, mapping)
        for digit in filter(lambda x: len(x) == 5, input):
            mapping[digit] = find_value(digit, mapping)
        total += int(''.join([str(mapping[digit]) for digit in output]))
    return total

def find_value(digit, mapping = {}):
    inverted_mapping = {v: k for k, v in mapping.items()}
    match len(digit):
        case 2:
            return 1
        case 3:
            return 7
        case 4:
            return 4
        case 7:
            return 8
        case 5:
            if contains_all(digit, inverted_mapping[1]):
                return 3
            elif contains_all(inverted_mapping[6], digit):
                return 5
            else:
                return 2
        case 6:
            if contains_all(digit, inverted_mapping[4]):
                return 9
            elif contains_all(digit, inverted_mapping[1]):
                return 0
            else:
                return 6

def parse_line(line):
    (input, output) = [[canonicalize(digit) for digit in io.split(' ')] for io in line.strip().split(' | ')]
    return (input, output)

def canonicalize(string):
    return ''.join(sorted(string))

def contains_all(haystack, needle):
    return all([c in haystack for c in needle])

if __name__ == "__main__":
    print(do(argv[1]))
    print(do2(argv[1]))
