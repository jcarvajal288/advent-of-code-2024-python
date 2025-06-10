import util
import re


def sum_of_corrupted_mul_instructions(filename):
    mul_regex = re.compile(r'mul\(\d+,\d+\)')
    number_regex = re.compile(r'\d+')
    corrupted_input = util.read_whole_file(filename)

    number_pairs = [number_regex.findall(match) for match in mul_regex.findall(corrupted_input)]
    return sum([int(match[0]) * int(match[1]) for match in number_pairs])