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
                             
