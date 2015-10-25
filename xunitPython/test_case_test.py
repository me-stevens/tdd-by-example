import unittest
from was_run   import WasRun
from test_case import TestCase

class TestCaseTest(TestCase):

  def setUp(self):
    self.test = WasRun("testMethod")

  def testTemplateMethod(self):
    test = WasRun("testMethod")
    test.run()
    assert("setUp " == self.test.log)
#    assert("setUp testMethod tearDown" == self.test.log)

  def testResult(self):
    test   = WasRun("testMethod")
    result = test.run()
    assert("1 run, 0 failed" == result.summary())

  def testFailedResult(self):
    test   = WasRun("testBrokenMethod")
    result = test.run()
    assert("1 run, 1 failed" == result.summary())
    
if __name__ == '__main__':
    unittest.main()

TestCaseTest("testTemplateMethod").run()

