#!/usr/bin/env python

from unittest import TestCase

from money.dollar import Dollar

class DollarsTest(TestCase):
    def testMultiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(Dollar(10), product)
        product = five.times(3)
        self.assertEqual(Dollar(15), product)

    def testEquality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))


if __name__ == '__main__':
    unittest.main()
