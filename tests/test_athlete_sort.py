import unittest
from challenges import athlete_sort


class TestSort(unittest.TestCase):
    def setUp(self):
        self.n = 5
        self.m = 3
        self.k = 1
        self.expected = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
        # self.expected = [[7, 1, 0], [10, 2, 5], [6, 5, 9], [9, 9, 9], [1, 23, 12]]
        self.result = [[7, 1, 0], [10, 2, 5], [6, 5, 9], [9, 9, 9], [1, 23, 12]]

    def testSort(self):
        self.assertListEqual(self.expected, self.result, "Lists not equal")


if __name__ == '__main__':
    unittest.main()

