#!/usr/bin/env python

from sys import argv
from ..util import read_to_strings

opening = ['{', '[', '(', '<']
closing = ['}', ']', ')', '>']
mapping = dict(zip(opening, closing))
scores = [1197, 57, 3, 25137]
corrupted_score_map = dict(zip(closing, scores))
incomplete_score_map = dict(zip(closing, [3,2,1,4]))

def do(input_file):
    lines = read_to_strings(input_file)
    sum = 0
    for line in lines:
        sum += find_value(line)
    return sum

def find_value(line):
    line = line.strip()
    stack = []
    for c in line:
        if(c in opening):
            stack.append(c)
        elif(c == mapping[stack[-1]]):
            stack.pop()
        else:
            return corrupted_score_map[c]
    return False

def do2(input_file):
    lines = read_to_strings(input_file)
    incomplete = filter(lambda x: not find_value(x), lines)
    sums = list(map(find_closing_score, incomplete))
    return sorted(sums)[int(len(sums)/2)]

def find_closing_score(line):
    line = line.strip()
    stack = []
    for c in line:
        if(c in opening):
            stack.append(c)
        elif(c == mapping[stack[-1]]):
            stack.pop()

    sum = 0
    for c in reversed(stack):
        sum *= 5
        sum += incomplete_score_map[mapping[c]]
    return sum

if __name__ == "__main__":
    print(do(argv[1]))
    print(do2(argv[1]))
