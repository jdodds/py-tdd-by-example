#!/usr/bin/env python

from unittest import TestCase

from money.currencies import Money, Dollar, Franc

class DollarsTest(TestCase):
    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def testFrancMultiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))

    def testEquality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))
        self.assertEqual(Franc(5), Franc(5))
        self.assertNotEqual(Franc(5), Franc(6))
        self.assertNotEqual(Franc(5), Dollar(5))


if __name__ == '__main__':
    unittest.main()
