from prelude.typeclasses import Monad
from prelude.decorators import singleton

class Maybe(Monad):
    @classmethod
    def mreturn(cls, val):
        return Just(val)

class Just(Maybe):
    def __init__(self, val):
        self.__val = val

    def __rshift__(self, f):
        return f(self.__val)

    def __repr__(self):
        return "Just({})".format(self.__val)

@singleton
class Nothing(Maybe):
    def __rshift__(self, f):
        return self

    def __repr__(self):
        return "Nothing"

