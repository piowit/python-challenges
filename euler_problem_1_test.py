# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# `python -m unittest euler_problem_1_test.py` to run the test

import unittest

class SumOfMultiplesTest(unittest.TestCase):

    def test_sum_for_below_10(self):
        self.assertEqual(23, SumOfMultiples().sum_for_below(10))

    def test_sum_for_below_1000(self):
        self.assertEqual(233168, SumOfMultiples().sum_for_below(1000))

class SumOfMultiples:

    def sum_for_below(self, n):
        x = 0
        for i in range(1, n):
            if i % 3 == 0 or i % 5 == 0:
                x += i

        return x

if __name__ == '__main__':
    unittest.main()
