# -*- coding: utf-8 -*-


"""py2nb.py2nb: provides entry point main()."""


__version__ = "0.2.0"


import sys
from .stuff import Stuff


def main():
    print("Executing py2nb version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))

class Boo(Stuff):
    pass
