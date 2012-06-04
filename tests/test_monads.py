import unittest
from prelude.monads import *


class MaybeTestCase(unittest.TestCase):

    """
    A test class for the Maybe monad
    """

    def testShortCircuit(self):
        self.assertEqual(Nothing(),
                         Just(42) >> \
                             (lambda x: Nothing()) >> \
                             (lambda x: Just(7)) )
                             

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
                              for z in Just(3)])
