TODO
====

Code
----
* more monads
* singly-linked lists
* list/sequence functions
...

Bugs
----
* using the monadic bind, currently both arguments to bind are
  evaluated even if the left side fails -- whereas using the iterator
  interface works fine

Packaging
---------
* use `setuptools` and post package on PyPI
