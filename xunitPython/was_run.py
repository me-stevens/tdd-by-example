from test_case import TestCase

class WasRun:

  def __init__(self, name):
    self.wasRun = None
    TestCase.__init__(self, name)

  def testMethod(self):
    self.wasRun = 1

