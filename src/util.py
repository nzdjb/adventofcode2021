"""Various utility functions."""

def read_to_ints(file_name: str) -> list[int]:
    """Read a file into an array of integers."""
    with open(file_name, encoding='UTF-8') as open_file:
        return [int(line.strip()) for line in open_file.readlines()]

def read_to_strings(file_name: str) -> list[str]:
    """Read a file into an array of strings."""
    with open(file_name, encoding='UTF-8') as open_file:
        return [line.strip() for line in open_file.readlines()]

def read_single_line_of_ints(file_name: str) -> list[int]:
    """Read a file containing a single line of comma separated ints."""
    with open(file_name, encoding="UTF-8") as open_file:
        return [int(i) for i in open_file.readline().strip().split(',')]

def read_to_int_lists(file_name: str) -> list[int]:
    """Read to a list of lists of ints."""
    with open(file_name, encoding="UTF-8") as open_file:
        return [[int(c) for c in line.strip()] for line in open_file]

