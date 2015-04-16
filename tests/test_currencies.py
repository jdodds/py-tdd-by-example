#!/usr/bin/env python

from unittest import TestCase

from finance.money import Money
from finance.bank import Bank
from finance.total import Total

class CurrencyTest(TestCase):
    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def testEquality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))
        self.assertNotEqual(Money.dollar(5), Money.dollar(6))
        self.assertNotEqual(Money.franc(5), Money.dollar(5))

    def testCurrency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def testSimpleAddition(self):
        five = Money.dollar(5)
        total = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(total, 'USD')
        self.assertEqual(Money.dollar(10), reduced)

    def testPlusReturnsTotal(self):
        five = Money.dollar(5)
        total = five.plus(5)
        self.assertEquals(five, total.augend)
        self.assertEquals(five, total.addend)

if __name__ == '__main__':
    unittest.main()
