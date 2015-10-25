import unittest
from was_run import WasRun

class TestWasRun(unittest.TestCase):

  def test_wasRun(self):
    test = WasRun("Test Method")
    print test.wasRun
    test.testMethod()
    print test.wasRun
