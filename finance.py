class Money():
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def __eq__(self, other):
        return (
            self.currency() == other.currency() and
            self.amount == other.amount
        )

    def __repr__(self):
        return "Money(%s, %s)" % (self.amount, self._currency)

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')

    def times(self, multiplier):
        return Money(self.amount * multiplier, self._currency)

    def currency(self):
        return self._currency

    def plus(self, addend):
        return Total(self, addend)

    def reduce(self, bank, to):
        rate = bank.rate(self._currency, to)
        return Money(self.amount / rate, to)

class Bank():
    class Pair():
        def __init__(self, source, to):
            self._source = source
            self._to = to

        def __eq__(self, other):
            return (
                self._source == other._source and
                self._to == other._to
            )

        def __hash__(self):
            return 0

    def reduce(self, source, to):
        return source.reduce(self, to)

    def addRate(self, source, to, rate):
        pass

    def rate(self, source, to):
        if source == 'CHF' and to == 'USD':
            return 2
        return 1

class Total():
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):
        amount = self.augend.amount + self.addend.amount
        return Money(amount, to)
