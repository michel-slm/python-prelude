import unittest
from prelude.typeclasses import Ord

def id(x):
    return x

class Transformed(Ord):
    def __init__(self, val, transformer=id):
        self.val = val
        self.set_transformer(transformer)

    def set_transformer(self, transformer):
        self.t = transformer
        self.tval = transformer(self.val)

    def __eq__(self, other):
        return self.t(self.val) == self.t(other)

    def __lt__(self, other):
        return self.t(self.val) < self.t(other)

class OrdTestCase(unittest.TestCase):

    """
    A test class for the Ord typeclass
    """

    def setUp(self):
        self.t001 = Transformed("one", len)
        self.t007 = Transformed("seven", len)
        self.t010 = Transformed("ten", len)
    
    def testLTE(self):
        self.assertTrue(self.t001 < self.t007.val)
        self.assertLess(self.t010, self.t007.val)

    def testGTE(self):
        self.assertGreater(self.t007, self.t010.val)
        self.assertGreater(self.t007, self.t001.val)
