import logging
import os
import os.path
import re
import sys


from biglib.locations.vertigo.common import find_home_dir


def test_find_home_dir():
    r, hd = find_home_dir()
    logging.debug(f"test_find_home_dir: {find_home_dir} returned {r} and {hd}")

    assert r
    assert os.getenv("HOME") == hd
