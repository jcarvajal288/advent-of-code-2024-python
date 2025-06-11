import util
import re

xmas_regex = re.compile(r'XMAS')
samx_regex = re.compile(r'SAMX')

def _count_in_lines(lines):
    xmas = [len(xmas_regex.findall(line)) for line in lines]
    samx = [len(samx_regex.findall(line)) for line in lines]
    return sum(xmas) + sum(samx)

def _count_forward_diagonal(lines):
    fdiag = [[] for _ in range(len(lines[0]) + len(lines) - 1)]
    for x in range(len(lines[0].strip())):
        for y in range(len(lines)):
            fdiag[x+y].append(lines[y][x])
    fdiag_strings = [''.join(line) for line in fdiag]
    return _count_in_lines(fdiag_strings)

def _count_backward_diagonal(lines):
    bdiag = [[] for _ in range(len(lines[0]) + len(lines) - 1)]
    min_index = -len(lines) + 1
    for x in range(len(lines[0].strip())):
        for y in range(len(lines)):
            bdiag[x-y-min_index].append(lines[y][x])
    bdiag_strings = [''.join(line) for line in bdiag]
    return _count_in_lines(bdiag_strings)

def count_xmas(filename):
    lines = util.read_lines_from_file(filename)
    horizontal_count = _count_in_lines(lines)
    transposed = [''.join(line) for line in [*zip(*lines)]]
    vertical_count = _count_in_lines(transposed)
    forward_diagonal_count = _count_forward_diagonal(lines)
    backward_diagonal_count = _count_backward_diagonal(lines)
    return horizontal_count + vertical_count + forward_diagonal_count + backward_diagonal_count