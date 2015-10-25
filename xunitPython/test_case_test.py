import unittest
from was_run   import WasRun
from test_case import TestCase

class TestCaseTest(TestCase):

  def testRunning(self):
    test = WasRun("testMethod")
    assert(not test.wasRun)
    test.run()
    assert(test.wasRun)


  def testSetUp(self):
    test = WasRun("testMethod")
    test.run()
    assert(test.wasSetUp)


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
