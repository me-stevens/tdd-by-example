from test_case import TestCase

class WasRun:

  def __init__(self, name):
    self.wasRun = None
    self.name   = name
    #TestCase.__init__(self, name)
    testcase    = TestCase(name)

  def testMethod(self):
    self.wasRun = 1

  def run(self):
    method = getattr(self, self.name)
    method()
