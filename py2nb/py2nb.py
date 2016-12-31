# -*- coding: utf-8 -*-


"""py2nb.py2nb: provides entry point main()."""


__version__ = "0.2.0"


import sys
from .toolbox import Base


def main():
    print("Executing py2nb version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print("Base and Extention():\n%s\n%s" % (Base, Extention()))

class Extention(Base):
    pass
