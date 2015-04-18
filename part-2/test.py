class WasRun:
    def __init__(self, name):
        self.wasRun = None

    def testMethod(self):
        self.wasRun = 1

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
