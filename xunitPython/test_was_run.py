import unittest
from was_run   import WasRun
from test_case import TestCase

class TestWasRun(unittest.TestCase):

  def testWasRun(self):
    test = WasRun("testMethod")
    print test.wasRun
    test.run()
    print test.wasRun

if __name__ == '__main__':
    unittest.main()
