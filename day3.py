import util
import re


def sum_of_corrupted_mul_instructions(filename):
    corrupted_input = util.read_whole_file(filename)
    return sum_mul_instructions(corrupted_input)


def sum_mul_instructions(corrupted_input):
    mul_regex = re.compile(r'mul\(\d+,\d+\)')
    number_regex = re.compile(r'\d+')
    number_pairs = [number_regex.findall(match) for match in mul_regex.findall(corrupted_input)]
    return sum([int(match[0]) * int(match[1]) for match in number_pairs])


def sum_of_enabled_mul_instructions(filename):
    corrupted_input = util.read_whole_file(filename)
    remove_regex = re.compile(r"(?s)don't\(\).*?do\(\)")
    cleaned_input = re.sub(remove_regex, '', corrupted_input)
    return sum_mul_instructions(cleaned_input)
