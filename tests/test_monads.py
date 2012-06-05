import unittest
from prelude.monads import *


class MaybeTestCase(unittest.TestCase):

    """
    A test class for the Maybe monad
    """

    def setUp(self):
        self.counter = 0

    def countingJust(self, val):
        self.counter += 1
        return Just(val)

    def testShortCircuit(self):
        self.assertEqual(Nothing(),
                         Just(42) >> \
                             (lambda x: Nothing()) >> \
                             (lambda x: Just(7)) )

    def testShortCircuit2(self):
        Nothing() >> self.countingJust
        self.assertEqual(0, self.counter)    

    def testIteration(self):
        self.assertEqual([(1,2,3)],
                         [(x,y,z) \
                              for x in Just(1) \
                              for y in Just(2) \
                              for z in Just(3)])

    def testIterationAbort(self):
        self.assertEqual([],
                         [(x,y,z) \
                              for x in Just(1) \
                              for y in Nothing() \
                              for z in self.countingJust(3)])
        self.assertEqual(0, self.counter)
