#!/usr/bin/env python
import os.path
from setuptools import setup, find_packages


version = __import__('checkio').__VERSION__
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fh:
    long_description = fh.read()

setup(
    name="checkio",
    version=version,
    packages=find_packages(),
    author="Joe Lei",
    author_email="thezero12@hotmail.com",
    description="checkio solution",
    long_description=long_description,
    license="IFOOTH",
    keywords="checkio",
    url="http://github.com/ifooth/checkio",
    classifiers=[
        'Programming Language :: Python',
    ],
)
