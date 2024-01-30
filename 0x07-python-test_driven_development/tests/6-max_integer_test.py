#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([4]), 4)
        self.assertIsNone(max_integer([]))

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_max_integer_mixed(self):
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, -2, -3, -4]), 1)

if __name__ == '__main__':
    unittest.main()
