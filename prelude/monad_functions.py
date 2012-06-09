def from_monad(m):
    """
    Returns the value of a monad
    """
    return m >> (lambda x: x)
