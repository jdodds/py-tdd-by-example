from .money import Money
from .total import Total

class Bank():
    def reduce(self, source, to):
        amount = source.augend.amount + source.addend.amount
        return Money(amount, to)
