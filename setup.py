#!/usr/bin/env python
import ast
import os
import re
import sys
from io import open

from setuptools import find_packages, setup

setup_dir = os.path.abspath(os.path.dirname(__file__))


setup(
    name="regpol",
    version="0.1.0",
    description="Read Windows Registry.pol files",
    maintainer="Joshua Pereyda",
    maintainer_email="joshua.t.pereyda@gmail.com",
    url="https://github.com/jtpereyda/pyregpol",
    packages=find_packages(exclude=[]),
    install_requires=[
        "click",
    ],
    extras_require={},
    python_requires=">=3.7",
    entry_points={"console_scripts": ["regpol=regpol:cli"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Security",
    ],
)
