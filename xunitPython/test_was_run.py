import unittest
from was_run import WasRun

class TestWasRun(unittest.TestCase):

  def test_wasRun(self):
    test = WasRun("testMethod")
    print test.wasRun
    test.run()
    print test.wasRun
