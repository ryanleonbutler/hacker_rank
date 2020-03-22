import unittest
from challenges import time_delta


t1 = "Sun 10 May 2015 13:54:36 -0700"
t2 = "Sun 10 May 2015 13:54:36 -0000"
t3 = "Sat 02 May 2015 19:54:36 +0530"
t4 = "Fri 01 May 2015 13:54:36 -0000"


class TestSum(unittest.TestCase):

    def test_time_delta1(self):
        self.assertEqual(time_delta.time_delta(t1, t2), 25200, "Should be 25200")
        self.assertEqual(time_delta.time_delta(t3, t4), 88200, "Should be 88200")


if __name__ == '__main__':
    unittest.main()
