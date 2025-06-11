import unittest

import day4


class MyTestCase(unittest.TestCase):
    def test_part1_sample(self):
        self.assertEqual(18, day4.count_xmas('./data/day4_sampledata.txt'))

    def test_part1_full(self):
        self.assertEqual(2370, day4.count_xmas('./data/day4_fulldata.txt'))


if __name__ == '__main__':
    unittest.main()
