class WasRun:
    def __init__(self, name):
        self.wasRun = None

    def testMethod(self):
        pass

test = WasRun("testMethod")
print(test.wasRun)
test.testMethod()
print(test.wasRun)
