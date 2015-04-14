from abc import ABCMeta, abstractmethod

class Money(metaclass=ABCMeta):
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return (
            type(self) == type(other) and
            self._amount == other._amount
        )

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)

    @abstractmethod
    def times(self, multiplier):
        pass

class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)
