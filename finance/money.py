class Money():
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return (
            self.currency() == other.currency() and
            self._amount == other._amount
        )

    def __repr__(self):
        return "Money(%s, %s)" % (self._amount, self._currency)

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def currency(self):
        return self._currency

    def plus(self, addend):
        return Money(self._amount + addend._amount, self._currency)
