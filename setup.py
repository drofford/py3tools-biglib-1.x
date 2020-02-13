from setuptools import setup, find_packages

import os
import os.path

project_name = "biglib"
program_name = project_name.replace("_", "-")

from importlib import import_module
from pathlib import Path

version_module = import_module(".version", package="src."+project_name)
VERSION = getattr(version_module, "VERSION")

setup(
    name=f"{project_name}",
    version=VERSION,
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=["attrs", "requests", "urllib3", "mako", "fuzzywuzzy", "python-levenshtein"],
    scripts=[],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
        # And include any *.msg files found in the "hello" package, too:
        "hello": ["*.msg"],
    },
    author="Garry A Offord",
    author_email="gofford@accertify.com",
    description="Big library of tools and APIs for various useful sh*t",
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
    entry_points={},
)
