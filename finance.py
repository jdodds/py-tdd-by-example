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
        if self._currency == 'chf' and to == 'USD':
            rate = 2
        else:
            rate = 1
        return Money(self.amount / rate, to)

class Bank():
    def reduce(self, source, to):
        return source.reduce(self, to)

    def rate(source, to):
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
