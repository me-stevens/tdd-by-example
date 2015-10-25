import unittest
from was_run   import WasRun
from test_case import TestCase

class TestWasRun(unittest.TestCase):

  def wasRun(self):
    test = WasRun(TestCase)
    print test.wasRun
    test.run()
    print test.wasRun
