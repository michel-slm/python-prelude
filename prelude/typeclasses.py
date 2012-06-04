from abc import ABCMeta, abstractmethod

class Eq(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __eq__(self, other):
        pass

    def __ne__(self, other):
        return not(self == other)

class Ord(Eq):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __lt__(self, other):
        pass

    def __le__(self, other):
        return (self < other) | (self == other)

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

class Monad(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def mreturn(cls, val):
        pass

    @abstractmethod
    def __rshift__(self, f):
        pass
