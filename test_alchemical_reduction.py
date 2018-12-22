import unittest
from alchemical_reduction import reduce_polymer

class TestReduction(unittest.TestCase):
    def test_reduce_polymer(self):
        testcases = [("dabAcCaCBAcCcaDA", "dabCBAcaDA"),
                     ("Aa", ""),
                     ("abBA", ""),
                     ("abAB", "abAB"),
                     ("aabAAB", "aabAAB")]
        for case in testcases:
            self.assertEqual(reduce_polymer(case[0]), case[1])

if __name__ == "__main__":
    unittest.main()
