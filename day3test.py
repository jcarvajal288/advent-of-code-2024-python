import unittest

import day3


class MyTestCase(unittest.TestCase):
    def test_part1_sample(self):
        self.assertEqual(161, day3.sum_of_corrupted_mul_instructions('./data/day3_sampledata.txt'))

    def test_part1_full(self):
        self.assertEqual(188192787, day3.sum_of_corrupted_mul_instructions('./data/day3_fulldata.txt'))

    def test_part2_sample(self):
        self.assertEqual(48, day3.sum_of_enabled_mul_instructions('./data/day3_sampledata.txt'))

    def test_part2_full(self):
        self.assertEqual(113965544, day3.sum_of_enabled_mul_instructions('./data/day3_fulldata.txt'))


if __name__ == '__main__':
    unittest.main()
