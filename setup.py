#!/usr/bin/env python
import ast
import os
import re
import sys
from io import open

from setuptools import find_packages, setup

setup_dir = os.path.abspath(os.path.dirname(__file__))


def find_version(*path_elements):
    """Search a file for `__version__ = 'version number'` and return version.

    @param path_elements: Arguments specifying file to search.

    @return: Version number string.
    """
    path = os.path.join(setup_dir, *path_elements)
    for line in open(path):
        for match in re.finditer(r"__version__\s*=\s(.*)$", line):
            return ast.literal_eval(match.group(1))
    raise RuntimeError("version string not found in {0}".format(path))


def get_long_description():
    descr = []
    for fname in "README.rst", "CHANGELOG.rst":
        with open(os.path.join(setup_dir, fname), encoding="utf-8") as f:
            descr.append(f.read())
    return "\n\n".join(descr)

extra_requirements = {
    "dev": ["tox", "flake8", "check-manifest"],
}


setup(
    name="regpol",
    version=find_version("regpol", "__init__.py"),
    description="Read Windows Registry.pol files",
    long_description=get_long_description(),
    maintainer="Joshua Pereyda",
    maintainer_email="joshua.t.pereyda@gmail.com",
    url="https://github.com/jtpereyda/regpol",
    packages=find_packages(exclude=[]),
    install_requires=[
        "click",
    ],
    extras_require=extra_requirements,
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
