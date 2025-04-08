import unittest
import day2

class TestDay2(unittest.TestCase):
    
    def test_part1_sample(self):
        self.assertEqual(day2.count_safe_reports('./data/day2_sampledata.txt'), 2)

    def test_part1_full(self):
        self.assertEqual(day2.count_safe_reports('./data/day2_fulldata.txt'), 332)

    def test_part2_sample(self):
        self.assertEqual(day2.count_safe_reports_with_dampener('./data/day2_sampledata.txt'), 4)

    def test_part2_full(self):
        self.assertEqual(day2.count_safe_reports_with_dampener('./data/day2_fulldata.txt'), 398)


if __name__ == '__main__':
    unittest.main()
        
