VERSION = "1.5.6"
program_name = "biglib"
description = """A command line app to send messages to Vertigo in the style of the Interceptas Control Room External Services page."""
requires = ["attrs", "requests", "urllib3", "mako", "fuzzywuzzy", "python-levenshtein"],

from setuptools import setup, find_packages

import os
import os.path

project_name = program_name.replace("-", "_")

from importlib import import_module
from pathlib import Path

version_module = import_module(".version", package="src."+project_name)
VERSION = getattr(version_module, "VERSION")

setup(
    name=program_name,
    version=VERSION,
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=requires,
    scripts=[],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        # "": ["*.txt", "*.rst"],
        # And include any *.msg files found in the "hello" package, too:
        # "hello": ["*.msg"],
    },
    author="Garry A Offord",
    author_email="gofford@accertify.com",
    description=description,
    license="(c) 2020 Accerty, Inc",
    keywords="external service vertigo dvs",
    url="http://www.accertify.com",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Copytight 2020 Accertify, Inc",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
    test_suite="py.test",
    tests_require=["pytest"],
