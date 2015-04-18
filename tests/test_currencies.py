#!/usr/bin/env python

from unittest import TestCase

from finance import Money, Total, Bank


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
        total = five.plus(five)
        self.assertEqual(five, total.augend)
        self.assertEqual(five, total.addend)

    def testReduceTotal(self):
        total = Total(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(total, 'USD')
        self.assertEqual(Money.dollar(7), result)

    def testReduceMoney(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), 'USD')
        self.assertEqual(Money.dollar(1), result)

    def testReduceMoneyDifferentCurrency(self):
        bank = Bank()
        bank.addRate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')
        self.assertEqual(Money.dollar(1), result)


if __name__ == '__main__':
    unittest.main()
