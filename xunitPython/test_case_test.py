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

if __name__ == '__main__':
    unittest.main()

TestCaseTest("testTemplateMethod").run()

