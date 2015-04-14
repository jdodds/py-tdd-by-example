class Dollar():

    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
