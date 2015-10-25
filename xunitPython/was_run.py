from test_case import TestCase

class WasRun:

  def __init__(self, name):
    self.wasRun   = None
    self.wasSetUp = 1
    self.name     = name
    self.log      = "setUp "
    #TestCase.__init__(self, name)
    testcase      = TestCase(name)

  def setUp(self):
    self.log = "setUp "

  def testMethod(self):
    self.log    = self.log + "testMethod" 

  def tearDown(self):
    self.log    = self.log + "tearDown"

  def run(self):
    method = getattr(self, self.name)
    method()

  def wasSetUp(self):
    self.wasRun   = None
    self.wasSetUp = 1
