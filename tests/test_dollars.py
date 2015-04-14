#!/usr/bin/env python

from unittest import TestCase

from money.dollar import Dollar

class DollarsTest(TestCase):
    def testMultiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

if __name__ == '__main__':
    unittest.main()
