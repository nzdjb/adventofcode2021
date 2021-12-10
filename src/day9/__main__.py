#!/usr/bin/env python

import math
from sys import argv
from ..util import read_to_int_lists

def do(input_file):
    lines = read_to_int_lists(input_file)
    sum = 0
    for (x, y) in find_low_points(lines):
        sum += lines[x][y] + 1
    return sum

def find_low_points(input):
    lines = [[10] + line + [10] for line in input]
    indexes = [[index for index in range(1, len(heights) - 1) if heights[index] < heights[index - 1] and heights[index] < heights[index + 1]] for heights in lines]
    lines = [(len(lines[0]) * [10])] + lines + [(len(lines[0]) * [10])]
    low_points = []
    for i in range(1, len(lines) -1):
        for j in indexes[i - 1]:
            height = lines[i][j]
            if(height < lines[i - 1][j] and height < lines[i + 1][j]):
                low_points.append((i - 1, j - 1))
    return low_points

def do2(input_file):
    lines = read_to_int_lists(input_file)
    sizes = [find_basin_size(x, y, lines) for (x, y) in find_low_points(lines)]
    return math.prod(sorted(sizes, reverse=True)[:3])

def find_basin_size(x, y, lines):
    return len(set(flatten(find_basin_size_int(x, y, lines))))

def find_basin_size_int(x, y, lines):
    val = lines[x][y]
    return [find_basin_size_int(a, b, lines) for (a, b) in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)] if a in range(0, len(lines)) and b in range(0, len(lines[0])) and lines[a][b] < 9 and lines[a][b] > val] + [(x, y)]

def flatten(lst):
    for entry in lst:
        if isinstance(entry, list):
            yield from flatten(entry)
        else:
            yield entry

if __name__ == "__main__":
    print(do(argv[1]))
    print(do2(argv[1]))
