import unittest
import day1

class TestDay1(unittest.TestCase):
    
    def test_part1_sample(self):
        self.assertEqual(day1.total_distance_between_lists('./data/day1_sampledata.txt'), 11)

    def test_part1_full(self):
        self.assertEqual(day1.total_distance_between_lists('./data/day1_fulldata.txt'), 2769675)

    def test_part1_part2_sample(self):
        self.assertEqual(day1.similarity_score('./data/day1_sampledata.txt'), 31)

    def test_part1_part2_full(self):
        self.assertEqual(day1.similarity_score('./data/day1_fulldata.txt'), 24643097)


if __name__ == '__main__':
    unittest.main()
        
