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

    def __init__(self):
        self._rates = {}

    def reduce(self, source, to):
        return source.reduce(self, to)

    def addRate(self, source, to, rate):
        self._rates[(source, to)] = rate

    def rate(self, source, to):
        if source == to:
            return 1
        return self._rates[(source, to)]

class Total():
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):
        amount = (self.augend.reduce(bank, to).amount +
                  self.addend.reduce(bank, to).amount)
        return Money(amount, to)

    def plus(self, addend):
        return Total(self, addend)

    def times(self, multiplier):
        return Total(
            self.augend.times(multiplier),
            self.addend.times(multiplier)
        )
