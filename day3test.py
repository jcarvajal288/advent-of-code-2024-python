import unittest

import day3


class MyTestCase(unittest.TestCase):
    def test_part1_sample(self):
        self.assertEqual(day3.sum_of_corrupted_mul_instructions('./data/day3_sampledata.txt'), 161)

    def test_part1_full(self):
        self.assertEqual(day3.sum_of_corrupted_mul_instructions('./data/day3_fulldata.txt'), 188192787)


if __name__ == '__main__':
    unittest.main()
