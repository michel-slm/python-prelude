from monad_functions import from_monad

def monad_eq(m_class):
    """
    injects an equality operator to a monadic class
    such that two monad instances are equal iff they are
    instances of the same monad class and their values
    are equal
    """
    def __eq__(self, other):
        return type(self) == type(other) and \
            from_monad(self) == from_monad(other)
    m_class.__eq__ = __eq__
    return m_class

def singleton(cls):
    """
    from PEP-0318 example by Shane Hathaway:
    http://www.python.org/dev/peps/pep-0318/#examples
    """
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance
