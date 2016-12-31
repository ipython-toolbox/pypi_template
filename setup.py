# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('py2nb/py2nb.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-py2nb",
    packages = ["py2nb"],
    entry_points = {
        "console_scripts": ['bootstrap = py2nb.py2nb:main']
        },
    version = version,
    description = "Python command line application Template.",
    long_description = long_descr,
    author = "Ralph Göstenmeier",
    author_email = "info@ralph-goesteneier.de",
    url = "http://blog.ralph-goestenmeier.de/",
    )
