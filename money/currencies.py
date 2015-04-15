from abc import abstractmethod

class Money():
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return (
            type(self) == type(other) and
            self._amount == other._amount
        )

    def __repr__(self):
        return "Money(%s, %s)" % (self._amount, self._currency)

    @staticmethod
    def dollar(amount):
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')

    @abstractmethod
    def times(self, multiplier):
        pass

    def currency(self):
        return self._currency

class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier, self._currency)

class Franc(Money):
    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)
