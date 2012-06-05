"""
from PEP-0318 example by Shane Hathaway:
http://www.python.org/dev/peps/pep-0318/#examples
"""
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance
