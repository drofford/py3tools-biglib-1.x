"""
Custom library used by my tools.

Library contains a bunch of tools for interceptas, vertigo, and miscellaneous purposes.
"""

__version__ = "2.0.3a2"

import logging, os

level = logging.DEBUG if os.getenv("DEBUG", "") == "Y" else logging.INFO
logging.basicConfig(format="%(asctime)s %(levelname)s : %(message)s", level=level)
