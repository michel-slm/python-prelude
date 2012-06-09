from abc import ABCMeta, abstractmethod
from prelude.typeclasses import Monad
from prelude.decorators import monad_eq, singleton

@monad_eq
class Either(Monad):
    __metaclass__ = ABCMeta

    @classmethod
    def mreturn(cls, val):
        return Right(val)

    @abstractmethod
    def __iter__(self):
        pass

class Left(Either):
    def __init__(self, val):
        self.__val = val

    def __rshift__(self, f):
        return self

    def __iter__(self):
        return iter([])

    def __eq__(self, other):
        return type(self) == type(other) 
    def __repr__(self):
        return "Left({})".format(self.__val)

class Right(Either):
    def __init__(self, val):
        self.__val = val

    def __rshift__(self, f):
        return f(self.__val)

    def __iter__(self):
        yield self.__val

    def __repr__(self):
        return "Right({})".format(self.__val)

class Maybe(Monad):
    __metaclass__ = ABCMeta

    @classmethod
    def mreturn(cls, val):
        return Just(val)

    @abstractmethod
    def __iter__(self):
        pass

@monad_eq
class Just(Maybe):
    def __init__(self, val):
        self.__val = val

    def __rshift__(self, f):
        return f(self.__val)

    def __iter__(self):
        yield self.__val

    def __repr__(self):
        return "Just({})".format(self.__val)

@singleton
class Nothing(Maybe):
    def __rshift__(self, f):
        return self

    def __iter__(self):
        return iter([])

    def __repr__(self):
        return "Nothing()"
