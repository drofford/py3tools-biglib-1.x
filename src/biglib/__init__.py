"""
Custom library used by my tools.

Library contains a bunch of tools for interceptas, vertigo, and miscellaneous purposes.
"""

__version__ = "2.4.0"

import logging
import os

import daiquiri

level = logging.DEBUG if os.getenv("DEBUG", "") == "Y" else logging.INFO
logging.basicConfig(format="%(asctime)s %(levelname)s : %(message)s", level=level)


daiquiri.setup(logging.DEBUG if os.getenv("DEBUG", "") == "Y" else logging.INFO)
logger = daiquiri.getLogger("biglib")
